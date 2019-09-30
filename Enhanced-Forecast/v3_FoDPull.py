
#! coding: utf-8
import requests, json, csv
import datetime
import pandas as pd
from dateutil.relativedelta import relativedelta

#緯度経度の定義
lat = '35.495'
lon = '138.991'

#API Keyの定義
apiKey = ''

url = 'https://api.weather.com/v3/wx/forecast/hourly/15day?geocode=' + lat + "," + lon

#パラメータの定義
payload = {'units': 'm', 'format': 'json', 'language': 'ja-JP'}
payload['apiKey'] = apiKey

data_dict = requests.get(url, params=payload).json()
data_str = json.dumps(data_dict)
df = pd.read_json(data_str)

df['validTimeLocal'] = pd.to_datetime(df['validTimeLocal'])
df['validTimeLocal'] = df['validTimeLocal'] + datetime.timedelta(hours=9) #JSTに変換（+9時間)

df.to_csv("filename.csv", index = False) #csvに出力
#df.to_csv("filename.csv", index = False, encoding = "shift-jis") #csv(shift-jis)に出力
