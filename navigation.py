#在导航中，进入商城即可开始进行购物
#舒识2021/6/10/17/46

from random import random, Random

navi ={
    "北京":{
        "朝阳区":{
            "公园":["朝阳公园","奥林匹克公园","北京欢乐谷"],
            "景点":["中国铁道博物馆","北京金港国际赛车场"],
            "商城":["凤凰汇购物中心","新七彩商业中心"]
        },
        "海淀区":{
            "高校":["清华大学","北京大学"],
            "景点":["圆明园","正觉寺"],
            "商城":["当代商城","领展购物广场"]
        },
        "东城区":{
            "景点":["天安门广场","故宫博物馆","人民英雄纪念碑"],
            "公园":["天坛公园","北海公园","景山公园"],
            "商城":["新世界百货","国瑞购物中心"]
        }

    },
    "上海":{
        "徐汇区":{
            "景点":["上海植物园","徐家汇天主教堂","上海龙华古寺"],
            "公园":["徐家汇公园","东安公园","漕溪公园"],
            "商城":["徐汇梅陇商业中心","西雅图"]

        },
        "浦东新区":{
            "景点":["东方明珠","金刚博物馆"],
            "公园":["迪士尼公园","华夏公园","世纪公园"],
            "商城":["比斯特上海购物村","绿地新都会"]
        },
         "奉贤区":{
            "景点":["头桥影剧院","九棵树未来艺术中心","胡桥影剧院"],
            "公园":["上海之鱼","上海海湾国家森林公园","碧海金沙"],
            "商城":["连城商业广场","蓝湾天地"]

        }

    },
    "广东":{
        "海珠区":{
            "景点":["黄埔古港景观区","广州水博苑"],
            "公园":["海珠湖公园","广州海珠国家湿地公园","瀛洲生态公园"],
            "商城":["珠影·星光城","万胜广场"]
        },
        "天河区":{
            "景点":["观音座莲","广东奥体中心"],
            "公园":["珠江公园","天河儿童公园","华南植物园"],
            "商城":["天河都市广场","M+Park漫广场"]
        },
        "白云区": {
            "景点": ["铜锣湾森林景区", "明珠楼"],
            "公园": ["陈田花园", "白云山原始森林公园", "南湖游乐园"],
            "商城": ["安华汇", "广州百信广场"]
        }

    }
}



def Navi_bar(navi):
    for i in navi:
        print(i)

key0 = 0

while True:
    print("请输入您想要去的城市")
    Navi_bar(navi)
    site1 = input()

    if site1 in navi:
        Navi_bar(navi[site1])
        print("请输入您想要去的区")
        site2 = input()
        if site2 in navi[site1]:
            Navi_bar(navi[site1][site2])
            print("请继续输入想去的地点，进入商城即可开启购物系统")
            site3 = input()
            if site3 in navi[site1][site2]:
                Navi_bar(navi[site1][site2][site3])
                print("请选择想要进入的地点")
                site4 = input()
                if site4 in navi[site1][site2][site3]:
                    print("欢迎您进入",site4,"导航结束")
                    if site3 == "商城":
                        key0 = 1
                        break
                    break
                else:
                    print("输入有误，将返回导航首页")

            else:
                print("输入有误，将返回导航首页")
        else:
            print("输入有误，将返回导航首页")

    else:
        print("输入有误，将返回导航首页")

if key0 == 1:

    #
    #
    # 进入商城，随机挑选商品进行半价，或者有购买该商品后可以进行全场满减
    #
    # 2021/6/9/11/10
    class GameShop:
        # 商品的名称和优惠状态，cost是原价，变为dis表示正在打折

        # 初始化列表
        def __init__(self, games):
            self.games = games

        # 单独商品折扣半价
        def discount(self, dis):
            self.dis = dis
            self.games[dis][2] = self.games[dis][2] / 2
            self.games[dis][3] = "dis"

        # 将商品的状态变为满减
        def max_minus(self, dis):
            self.games[dis][3] = "可满减"

        # 获得整个列表
        def getGames(self):
            print("\t\t\t\t商城\t\t\t\t\t")
            print("商品序号\t", "名称", "\t\t\t价格", "\t\t\t状态")
            for i, name, price, state, amout in self.games:
                print(i, "\t\t", name, "\t\t", price, "\t\t\t", state)


    # 依次分别是商品序号，商品名称，商品价格，商品折扣状态，商品已被添加到购物车次数
    games = [
        [1, "gta5  ", 180, "cost", 0],
        [2, "巫师3  ", 90, "cost", 0],
        [3, "上古卷轴5", 50, "cost", 0],
        [4, "传送门2  ", 30, "cost", 0],
        [5, "往日不在", 298, "cost", 0],
        [6, "战地风云5", 228, "cost", 0],
        [7, "NBA 2K21", 199, "cost", 0],
        [8, "极品飞车22", 200, "cost", 0],
        [9, "双人成行", 198, "cost", 0],
        [10, "无主之地3", 198, "cost", 0]
    ]
    # money就是全场的余额
    print("请输入您的余额")
    money = int(input())
    # max_max
    max_max = 0
    max1 = 0
    long_money = money

    steam = GameShop(games)
    loan = int(random() * 20)
    shop_cat = [

    ]
    max = 0
    if loan < 10:
        print("恭喜您获得了", steam.games[loan][1], "商品半价的优惠")
        steam.discount(loan)
        max = loan
    else:
        print("恭喜您获得了购买", steam.games[loan - 10][1], "商品即可全场满600减300的优惠")
        steam.max_minus(loan - 10)
        max = loan

    while True:
        p = long_money - money
        if max > 10 and steam.games[max - 10][4] != 0:
            if max1 == 0 and p >= 600:
                money = money + 300
                max1 += 1

        steam.getGames()
        print("请输入")
        print("您目前的余额为", money)
        print("将商品添加至购物车--1\t查看购物车--2\t\t结算--3\t\t离开商场--4")
        key = int(input())
        while key == 1:
            print("请输入您想购买的商品的商品序号")
            id = int(input())
            if id > 10 or id <= 0:
                print("没有该商品，返回主页面")
                break
            elif money < games[id - 1][2]:
                print("余额已不足，请充值，将返回主页面")
                break
            else:
                print("添加购物车成功，将返回主界面")
                if steam.games[id - 1][4] == 0:
                    steam.games[id - 1][4] += 1
                    money = money - steam.games[id - 1][2]
                    shop_cat.append(
                        [steam.games[id - 1][0], steam.games[id - 1][1],
                         steam.games[id - 1][2], steam.games[id - 1][3],
                         steam.games[id - 1][4]])
                    break
                else:
                    i = 0
                    while steam.games[id - 1][0] != shop_cat[i][0]:
                        i += 1
                    shop_cat[i][4] += 1
                    shop_cat[i][2] = shop_cat[i][2] + steam.games[id - 1][2]
                    money = money - steam.games[id - 1][2]
                    break

        while key == 2:
            if len(shop_cat) == 0:
                print("购物车为空，将返回主页面")
                break
            print("\t\t\t\t购物车\t\t\t\t\t")
            print("名称", "\t\t\t价格", "\t\t\t状态", "\t\t\t购买数量")
            for i, name, price, state, amout in shop_cat:
                print(name, "\t\t\t", price, "\t\t\t", state, "\t\t\t", amout)
            if max < 10:
                i = 0
                m = 0
                while i < len(shop_cat):
                    m = m + shop_cat[i][2]
                    i += 1
                max_max = steam.games[max][2] * steam.games[max][4]
                print("目前总金额为", m, "已优惠", max_max)
                max_max = 0

            else:
                i = 0
                m = 0
                while i < len(shop_cat):
                    m = m + shop_cat[i][2]
                    i += 1

                if steam.games[max - 10][4] == 0:
                    print("目前总金额为", m)
                    print("你还需要购买满减商品才能享受满减")

                    break
                elif m < 600:
                    print("目前总金额为", m)
                    print("您还需要购买", 600 - m, "元才能享受满减")
                    break
                else:
                    print("目前总金额为", m - 300, "已优惠300元")

                    break

            print("输入随意数字退出购物车界面")
            input()
            break

        if key == 3:
            print("您购买了")
            print("名称", "\t\t\t价格", "\t\t\t购买数量")
            for i, name, price, state, amout in shop_cat:
                print(name, "\t\t\t", price, "\t\t\t", amout)

            i = 0
            m = 0
            while i < len(shop_cat):
                m = m + shop_cat[i][2]
                i += 1

            if max < 10:
                max_max = steam.games[max][2] * steam.games[max][4]
            else:
                if max1 == 1:
                    max_max = 300
                    m = m - 300

            if max_max > 0:
                print("您优惠了", max_max, "元")

            print("您消费了", m, "元")
            m = int(m / 10)
            print("您获得了", m, "积分")
            print("您还剩下", money, "元")
            break

        if key == 4:
            print("您放弃了购物，一分钱也没买，默默离开了此地")
            break
