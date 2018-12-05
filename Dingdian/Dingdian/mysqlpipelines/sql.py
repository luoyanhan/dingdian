import pymysql
from Dingdian import settings


MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB


cnx = pymysql.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, port=MYSQL_PORT, db=MYSQL_DB)
cur = cnx.cursor()


# language1 = """DROP TABLE IF EXISTS dd_chaptername;"""
# language2 = """create table dd_chaptername(
# id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
# xs_chaptername varchar(255) DEFAULT NULL,
# xs_content text ,
# id_name int(11) DEFAULT NULL,
# num_id int(11) DEFAULT NULL,
# url varchar(255) DEFAULT NULL
# )ENGINE=InnoDB AUTO_INCREMENT=2726 DEFAULT CHARSET=gbk;"""
# language3 = """SET FOREIGN_KEY_CHECKS=1;"""
# sql = """create table dd_name(
#           id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
#           xs_name varchar(255) DEFAULT NULL,
#           xs_author varchar(255) DEFAULT NULL,
#           category varchar(255) DEFAULT NULL,
#           name_id varchar(255) DEFAULT NULL
#           ) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8"""
# print(cur.fetchall())

# pymysql.err.InterfaceError: (0, '')

# cur.execute('SELECT * FROM dd_name')
# print(cur.fetchall())
# print(cur.fetchall())
# cnx.commit()

# {'chaptercontent': '“这人是谁？难道在找死吗？居然敢跟王源争抢水仙花，难道他就不怕走不出绝情郡。顶点小说 '
#                    "Ｘ２３ＵＳ．ＣＯＭ更新最快”大厅之中一个刀疤男子道：“找死的人不是他，而是你吧，能进入贵宾间的人能有几个是简单的，你这样议论不怕死吗。”刀疤男子身边一个青年男子道：听到此话刀疤男子马上闭上了嘴。“一千灵石一次，还有更高的吗？”方天佐的声音传遍了整个交易场四周。三楼的一间贵宾室之内，“这个人是谁居然出手这么大方，我也只是买回去给宗门储存，宗门不可能给我太多的东西，在出价的话就有些划不来了。”王源并没有再次出价。方天佐看了三楼一眼，看到没有人继续出价，心想！一株水仙花市场价最多五百三阶灵石，现在一千三阶灵石已经是赚了一倍，还想再抬高价格基本上是不可能。然后高声道：“一千灵石两次，一千灵石第三次，成交。”接下来第六件、第七件、第八件宝物张凡并没有出手，因为这些宝物对张凡用处不大，这三件宝物被二楼与三楼贵宾室里的人购买了。三天佐清了清嗓子，整理了一下衣服，带着神秘的笑容道：“接下来的这件宝物便是今天最后一件宝物，也是本场恒大交易会的压轴宝物。'四转化毒丹'出自飘渺仙宗四阶鬼丹大师之手，相信大家从名字中就能听出这颗丹药的功效，那就是排污解毒！起拍价一百块四阶灵石，每次加价不得少于十块，现在开始拍卖。”这东西在特殊的地点可是保命的好东西，所以出价的人还是很多。不到一会儿时间便被抬到了三百块，三百块这可是四阶灵石！如果换成三阶灵石的话，至少也能换三万块！这基本上是一个二流宗门的一半财产。二楼张凡所在贵宾间内。蔡文姬没有了平时的高冷与抚媚，这时蔡文姬双拳紧紧的握在一起，双眼死死的看着大厅之内颗丹药！脸上显出无限的紧张之色，这次她便是冲着这颗丹药来的。张凡把一只手放在蔡文姬的芊芊玉手之上；另一只手拍了拍蔡文姬的肩膀，用温文尔雅的声音道：“放松，就算你十分的需要这颗丹药，也不要太过的紧张！否则只能让你失去理智，并不能让你得到这颗丹药。能告诉我你为什么需要这个丹药吗？”蔡文姬深呼了几口气，平复一下紧张的心情！用略显紧张的声音道：“谢谢你小凡弟弟！我娘亲中了一种剧毒，所以我需要这棵丹药，只要能得到这颗丹药不论付出任何代价我都愿意。”此时这棵四阶丹药已经被抬到了四百块四阶灵石！虽然价格被抬高了许多，但是竞价的人却只有了一家。蔡文姬略星紧张的声音道“五百块四阶灵石。”要知道自己全部身家也才八百块四阶灵石，要是有人超过自己的身家怎么办！等了半响之后，并没有人继续出价，上一个出价值之人也没有继续出价了，蔡文姬的紧张之色才慢慢的平复了下来。方天佐见没人出阶朗声道：“五百块四阶灵石一次，还有没有更高的。五百块四阶灵石第二次，确定没有更高了。五百块四阶灵石…………”就在这时三楼一号贵宾室内，发出了一道慵懒的声音！“六百块四阶灵石。”蔡文姬喃喃自语道：“他还是出手了，看来躲是躲不过了！六百五十块四阶灵石。”那个慵懒的声音毫不犹豫的道：“七百块四阶灵石！文姬只要你答应做我的女人，我就将这颗四阶灵丹让给你，否则的话你母亲可能就真的没救了。”张凡看着蔡文姬，不动声色的道：“这个家伙是谁，他怎么对你好像很了解。”蔡文姬咬牙切齿的道：“此人是绝情宗当代宗主之子，更是绝情宗上代宗主元婴期高手之孙绝魂。而且好色至极！”蔡文姬并没有接绝魂的话，而是继续道：“八百块四阶灵石。”三楼一号贵宾室内，四个是待女正在卖力的给绝魂按摩！绝魂捏了捏一个待女的胸！哈哈大笑！那笑声十分的淫荡，“文姬你争不过我的，还是快投入我的怀抱吧，我出一千块四阶灵石。”听到绝魂再次出价，蔡文姬整个身子都软了下去。口中喃喃自语道：“难道只能……，看来这就是天命。”转眼间蔡文姬已经满脸泪痕。要知道一般的四阶丹药也就值一百块四品灵石，就算这颗丹药比较特殊！能拍出三百块四阶灵石已经是最好了，没有想到的是居然拍出了一千块四阶灵石的天价。方天佐从愣神回了过来，皮笑肉不笑的道：“一千块四阶灵石一次，还有没有更高的。”张凡拍了拍蔡文姬的背，然后大声的道：“我出价二十块五阶灵石。”蔡文姬先是一喜，然后便满脸的愁容小声的对着张凡道：“小凡弟弟，如果没有那么多灵石的话，最好赶紧放弃竞价！我知道你想帮我，但是在恒大交易会胡乱竞价事后没有足够灵石交易！就算是筑基期大圆满之人也会被抹杀。”张凡平淡的说道：“姬姐姐放心，这点灵石我还是有的，你已经帮助我那么多了，是时候该我帮助你一次了。”大厅中满脸刀疤的男子暗暗自语道：“刚才我议论那个人居然有五阶灵石，我真是老寿星上吊找死。这种人要么是背景不简单、要么自身实力不凡！还好我没说他坏话。”绝魂也不是那种没有脑子之人，能拿出五阶灵石之人绝不简单。绝魂一改常态郑重的道：“阁下是何许人，能否卖我绝魂一个面子，他日必有厚报。”张凡并没有理会绝魂这种人，而是对着大厅高台之上方天佐道：“如果没有人继续出价，我希望尽快宣布这棵四丹药的归属。”绝魂此时面色扭曲，手中的劲越来越大捏得待女的胸部都变了形，不过待女虽然疼痛难忍，但却没有叫出来。因为他知道现在叫出来的话等待自己的只有一个字'死'！不过他并没有继续出价，而是死死的盯住二楼张凡所在的贵宾室。",
#  'chaptername': '第一百二十六章帮助',
#  'chapterurl': 'https://www.x23us.com/html/70/70627/31027949.html',
#  'id_name': '70627',
#  'num': 126}

class Sql():
    @classmethod
    def insert_dd_name(cls, xs_name, xs_author, category, name_id):
        global cnx
        global cur
        try:
            cnx.ping(reconnect=True)
            cur = cnx.cursor()
            sql = """INSERT INTO dd_name (xs_name, xs_author, category, name_id) VALUES ('%s', '%s', '%s', '%s');""" % (
            str(xs_name), str(xs_author), str(category), str(name_id))
            cur.execute(sql)
            cnx.commit()
        except Exception as e:
            print(e)
            with open('./ERROR.txt', 'a+') as f:
                f.write(e)
                f.write('\n')



    @classmethod
    def select_name(cls, name_id):
        global cnx
        global cur
        try:
            cnx.ping(reconnect=True)
            cur = cnx.cursor()
            sql = """SELECT EXISTS(SELECT 1 FROM dd_name WHERE name_id={0});""".format(str(name_id))
            cur.execute(sql)
            return cur.fetchall()[0]
        except Exception as e:
            print(e)
            with open('./ERROR.txt', 'a+') as f:
                f.write(e)
                f.write('\n')

    @classmethod
    def insert_dd_chaptername(cls, xs_chaptername, xs_content, id_name, num_id, url):
        global cnx
        global cur
        try:
            cnx.ping(reconnect=True)
            cur = cnx.cursor()
            sql = """INSERT INTO dd_chaptername (xs_chaptername, xs_content, id_name, num_id, url) VALUES ('%s', '%s', '%s', '%s', '%s');""" % (str(xs_chaptername), str(xs_content), int(id_name), int(num_id), str(url))
            cur.execute(sql)
            cnx.commit()
        except Exception as e:
            print(e)
            with open('./ERROR.txt', 'a+') as f:
                f.write(url)
                f.write(e)
                f.write('\n')

    @classmethod
    def select_chapter(cls, url):
        global cnx
        global cur
        try:
            cnx.ping(reconnect=True)
            cur = cnx.cursor()
            sql = """SELECT EXISTS(SELECT 1 FROM dd_chaptername WHERE url='%s');"""%(str(url))
            cur.execute(sql)
            return cur.fetchall()[0]
        except Exception as e:
            print(e)
            with open('./ERROR.txt', 'a+') as f:
                f.write(url)
                f.write(e)
                f.write('\n')