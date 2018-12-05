import scrapy
from Dingdian.items import DingdianItem, DcontentItem
from Dingdian.mysqlpipelines.sql import Sql

class DingdianSpider(scrapy.Spider):
    name = 'dingdian'
    baseurl = 'https://www.x23us.com/class/'

    def start_requests(self):
        for i in range(1, 11):
            url = self.baseurl + str(i) + '_1.html'
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        maxnum = response.xpath(r'//a[@class="last"]/text()').extract_first()
        bashurl = str(response.url)[:-6]
        for i in range(1, int(maxnum)+1):
            new_url = bashurl + str(i) + '.html'
            yield scrapy.Request(new_url, callback=self.get_name)

    def get_name(self, response):
        trs = response.xpath(r'//tr[@bgcolor="#FFFFFF"]')
        for tr in trs:
            novelname = tr.xpath(r'./td[1]/a[@target="_blank"]/text()').extract_first()
            novelurl = tr.xpath(r'./td[1]/a[@target="_blank"]/@href').extract_first()
            author = tr.xpath(r'./td[3]/text()').extract_first()
            wordnumber = tr.xpath(r'./td[4]/text()').extract_first()
            status = tr.xpath(r'./td[6]/text()').extract_first()
            yield scrapy.Request(novelurl, callback=self.get_chapterurl, meta={'novelurl': novelurl,
                                                                               'novelname': novelname,
                                                                               'author': author,
                                                                               'wordnumber': wordnumber,
                                                                               'status': status
                                                                               })

    def get_chapterurl(self, response):
        item = DingdianItem()
        item['name'] = response.meta['novelname']
        item['novelurl'] = response.meta['novelurl']
        item['author'] = response.meta['author']
        item['status'] = response.meta['status']
        item['wordnumber'] = response.meta['wordnumber']
        item['category'] = response.xpath(r'//div[@class="bdsub"]/dl/dt/a[2]/text()').extract_first()
        name_id = response.url.split('/')[-2]
        item['name_id'] = name_id
        yield item
        num = 0
        urls = response.xpath(r'//td[@class="L"]')
        for url in urls:
            href = url.xpath(r'./a/@href').extract_first()
            chapter_name = url.xpath(r'./a/text()').extract_first()
            if href and chapter_name:
                chapter_url = response.url + href
                rets = Sql.select_chapter(chapter_url)
                if rets[0] == 1:
                    print('章节已经存在', chapter_url)
                else:
                    num += 1
                    yield scrapy.Request(chapter_url, callback=self.get_chaptercontent, meta={'name_id': name_id,
                                                                                              'num': num,
                                                                                              'chapter_url': chapter_url,
                                                                                              'chapter_name': chapter_name})

    def get_chaptercontent(self, response):
        item = DcontentItem()
        item['num'] = response.meta['num']
        item['id_name'] = response.meta['name_id']
        item['chaptername'] = response.meta['chapter_name']
        item['chapterurl'] = response.meta['chapter_url']
        content = response.xpath(r'//dd[@id="contents"]').xpath('string(.)').extract_first()
        item['chaptercontent'] = str(content).replace('\xa0', '')
        yield item
