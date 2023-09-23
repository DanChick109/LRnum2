import requests

s_city = "Moscow"
appid = 'ca74b8c282b00eb346a4330255186f41'

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", s_city)
print("Скорость ветра:", data['wind']['speed'])
print("Видимость:", data['visibility'])
print()

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nВидимость:  <",
          '{0:+3.0f}'.format(i['visibility']), ">")
    print("Скорость ветра:  <",
          '{0:+3.0f}'.format(i['wind']['speed']), ">")
    print("Температура:  <",
          '{0:+3.0f}'.format(i['main']['temp']), ">")
    print("----------------------------")
