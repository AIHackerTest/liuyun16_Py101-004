import requests
import json

def json_parse(json_xinzhi, unit):
    """
    专用于心知天气的API json类型的response解析
    """
    r1=json_xinzhi.json() #或者r1=json.loads(r.text),得到的是dict{}类型，
    if 'results' in r1:
        city_result=r1['results'][0]['location']['name']
        wea_now=r1['results'][0]['now']['text']
        temp_now=r1['results'][0]['now']['temperature']
        last_upd=r1['results'][0]['last_update'][:-6].replace("T"," ")
        if unit == 'f':
            temp_now_f = temp_conv(temp_now)
            temp_now= "{} {}".format(temp_now_f, '华氏度')
            print(f"您查询的城市：{city_result},当前天气为:{wea_now}，{temp_now},数据更新时间：{last_upd}")
        else:
            temp_now = "{} {}".format(temp_now, '摄氏度')
            print(f"您查询的城市：{city_result},当前天气为:{wea_now}，{temp_now},数据更新时间：{last_upd}")
        result={'城市':city_result, '当前天气': wea_now, '温度':temp_now,'更新时间':last_upd}
        return result
    else:
        print("对不起，当前系统暂不支持您所查询的城市。")
        result = None
        return result

def xz_para(loca):
    para={
            'key': 'r7rnc5ggi9g3xpxv',
            'location': loca,
            'language': 'zh-Hans', # 可缺省为中文简体
            'unit':'c'# 可缺省为c摄氏度。参数不能加空格。
            }
    return para

def hist_inq(result_hist, hist_log=[]):
    hist_once={} #内部变量在循环中，每次都会归零，岂不是不可以累加历史？可以考虑用文件实现？
    for x, v in result_hist.items():
        hist_once[x]=v
    hist_log.append(hist_once)
    return hist_log

def list_dict_print(list_dict, j=0):
    for x in list_dict:
        j+=1
        print(f"第{j}次查询：")
        for u, v in x.items():
            if u == "温度":
                print(f"{u}:{v},",end =" ") #利用print函数，控制显示在一行
            else:
                print(f"{u}:{v}",end =",")
        print("\n")

def help_wea():
    print ("""
   输入城市名，返回该城市最新的天气数据；
   输入h 或 help，获取帮助信息；
   输入history或历史，获取历史查询信息（一般使用 history）；
   输入q，quit，exit，退出程序的交互。
   输入f，查询温度结果以华氏度显示，输入c, 则以摄氏度显示。
    """)

def temp_conv(temp_u_C, temp_u_F = 0.0):
    temp_u_F=float(temp_u_C)*1.8+32 #注意temp_u_C为str类型；
    str("{0:.1f}".format(temp_u_F)) #保留1位小数。
    return temp_u_F

Flag = True
log=[]
unit_d='c'

print("欢迎使用云天气，天气数据由心知天气提供, 目前程序仅支持全国地级城市查询服务。")
try:
    while Flag:
        next = input("请输入城市名或指令：\n")
        next=next.replace(" ","")
        if next in ['h','help']:
            help_wea()
        elif next in ['history', '历史']:
            print("查询历史:")
            list_dict_print(log)
        elif next not in ['q','quit','exit']:
            if next in ['f']:
                print("您查询的结果将以华氏度显示。")
                unit_d = 'f'
                continue
            if next in ['c']:
                print("您查询的结果将以摄氏度显示。")
                unit_d = 'c'
                continue
            input_next=xz_para(next)
            r =requests.get('https://api.seniverse.com/v3/weather/now.json', input_next)
            r_j=json_parse(r, unit_d)
            if r_j:
                log=hist_inq(r_j)
        else:
            print("即将退出程序，谢谢使用！")
            Flag = False
except EOFError:
    print("您强制退出了，谢谢使用，再见！")
