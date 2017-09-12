from flask import render_template,Flask, request, url_for
import requests
import json
import sqlite3

app = Flask(__name__)
log = []

conn = sqlite3.connect(r"myweather.db")  # 如果数据库不存在则创建，并建立连接，连接对象为conn
cur = conn.cursor()  # 创建游标对象，
cur.execute('''CREATE TABLE IF NOT EXISTS cityweather
            (cityname text, weather text, temperature text, inqueytime text )''')  # 游标对象才有excute属性，
conn.commit() # 提交更改，否则可能不能保存。


@app.route("/", methods = ['GET','POST'])
def index():
    help_get = 0
    log_flag = 0
    weather_result = None

    print(request.form)
    if request.form.get("btn") == "历史":
        log_flag = 1
    elif request.form.get("btn") == "帮助":
        help_get = 1
    elif request.form.get("city"):
        city_in = request.form.get("city")
        input_next = xz_para()
        r =requests.get('https://api.seniverse.com/v3/weather/now.json', input_next) #可以考虑完全封装到fetchweather 函数中。
        weather_result = json_parse(r, "c")
        print(f"weather_result is {weather_result}")
        upd_db(weather_result)
        if weather_result:
            log.append(weather_result) #将查询结果增补到历史log变量中。
            upd_db(weather_result)
            print(log)
        else:
            print("未查询到改城市，请您再次输入！")
    return render_template('home_form.html', help_get = help_get, weather_result = weather_result, log = log, log_flag = log_flag)


def xz_para():
    para={
            'key': 'r7rnc5ggi9g3xpxv',
            'location': request.form.get("city"), #尝试从form表单中获取用户输入城市名；
            'language': 'zh-Hans',
            'unit':'c'
            }
    return para

def json_parse(json_xinzhi, unit):
    """
    专用于心知天气的API json类型的response解析
    """
    r1=json_xinzhi.json()
    if 'results' in r1:
        city_result=r1['results'][0]['location']['name']
        wea_now=r1['results'][0]['now']['text']
        temp_now=r1['results'][0]['now']['temperature']
        last_upd=r1['results'][0]['last_update'][:-6].replace("T"," ")
        temp_now = "{} {}".format(temp_now, '℃')
        print(f"您查询的城市：{city_result},当前天气为:{wea_now}，{temp_now},数据更新时间：{last_upd}")
        result = {'城市':city_result, '当前天气': wea_now, '温度':temp_now,'更新时间':last_upd}

    else:
        print("对不起，当前系统暂不支持您所查询的城市。")
        result = None

    return result

def upd_db(dict1):
    conn1 = sqlite3.connect(r"myweather.db")
    cur1 = conn1.cursor()  # 创建游标对象，
    tuple_db = (dict1.get('城市'), dict1.get('当前天气'), dict1.get('温度'), dict1.get('更新时间'))
    print(tuple_db)
    cur1.executemany('INSERT INTO cityweather VALUES (?,?,?,?)' , (tuple_db,))
    cur1.execute('SELECT * from cityweather')
    conn1.commit()
    return cur1.lastrowid


if __name__ == '__main__':
    app.run(debug = 1)
