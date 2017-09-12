# -*- coding: utf-8 -*-
"""A weather-inquiry system."""
import requests
from flask import Flask, render_template, request


app = Flask(__name__)
history_weather = []


def inquiryWeather(city):
    """Download the real-time weather from hefeng.com according city."""
    key = "bbd1ac758b5d464e8d1d63a58ef015f9"
    url = 'https://free-api.heweather.com/v5/now?city=' + city + '&key=' + key
    weather = requests.get(url)
    weather_info = eval(weather.text)['HeWeather5'][0]
    result = {}
    if weather_info['status'] != 'ok':
        raise KeyError
    else:
        result['city'] = city
        result['cond_txt'] = weather_info['now']['cond']['txt']
        result['wind_dir'] = weather_info['now']['wind']['dir']
        result['tmp'] = weather_info['now']['tmp']
        history_weather.append(result)
        return result


@app.route("/", methods=['GET', 'POST'])
def main():
    """Render web pages."""
    weather = None
    history = None
    get_help = None
    error = None
    if request.method == 'POST':
        if request.form['action'] == u'查询':
            try:
                weather = inquiryWeather(request.form['city'])
            except KeyError:
                error = 1
        elif request.form['action'] == u'历史':
            history = history_weather
        else:
            get_help = 1
    return render_template(
        'weatherInquiry.html',
        weather=weather, history=history, get_help=get_help, error=error)


if __name__ == '__main__':
    app.run(debug=True)
