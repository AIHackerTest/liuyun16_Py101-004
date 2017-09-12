# -*- coding: utf-8 -*-
"""
完成一个最简天气查询程序，运行在命令行界面，实现以下功能：

输入城市名，返回该城市的天气数据；
输入指令，打印帮助文档（一般使用 h 或 help）；
输入指令，退出程序的交互（一般使用 quit 或 exit）；
在退出程序之前，打印查询过的所有城市。
"""
city_dic={}
hist_check={}
Flag = True

with open('C:/git\Py101-004/Chap1/resource/weather_info.txt', 'r',encoding='utf-8') as f_w:
    for p in f_w:# 这一行已经包括了readline操作，下一行再用readline()则会再次到下一行。
        p1=None
        p1=p.strip('\n').split(",") #得到的字符串的内容去掉\n; 将得到的字符串内容，用逗号，隔开为多个字符串的list
        city_dic.update({p1[0]:p1[1]})# 构建city-weather作为key-value的dict。

while Flag == True:
    next=input("请输入城市名或指令：\n")

    if next in city_dic:
        a = city_dic.get(next)
        hist_check[next] =  a
        print(f"您查询的城市天气为:{a}")

    elif next not in city_dic:
        if  next=='h' or next == 'help':
            print ("""
            输入城市名，返回该城市的天气数据；
            输入指令（h 或 help），打印帮助文档；
            输入指令（ quit 或 exit），退出程序的交互；
            在退出程序之前，程序打印查询过的所有城市。
            """)
        elif next == "quit" or next == "exit":
            Flag = False
            print(f"您的查询历史为：")
            for x, v in hist_check.items(): #必须要items()方法，否则打印的并非key-value pair。
                print(f"城市：{x},天气：{v}")

        else:
            print("对不起，您的输入有误，可重新输入（输入h或者help获取帮助）")
