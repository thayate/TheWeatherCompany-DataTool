#Created by Hayate Takada, The Weather Company, IBM Japan

import requests, datetime, time
import pandas as pd
from dateutil.relativedelta import relativedelta
import io

#取得するポイントリストを読み込む
locations = pd.read_csv("pointList.csv", dtype=str)

#API Keyを入力
apiKey = ''

#日本時間で取得を開始する日時を入力する
print('日本時間でデータを取得開始する日時を入力してください。フォーマットはYYYY/MM/DD HH:00。例: 2016/02/04 06:00')
localStartDateTime = input()

#何ヶ月分のデータを取得するかを入力する
print('何ヶ月分のデータを取得しますか？整数値で記載してください。')
months = input()
months = int(months)

#入力した日付をAPIパラメータ用に定義しなおす(日付型に変換→UTC時間に変換)
formmated_localStartDate = datetime.datetime.strptime(localStartDateTime, "%Y/%m/%d %H:%M")
formmated_localEndDate = formmated_localStartDate + relativedelta(months=1) - datetime.timedelta(hours=1)

formmated_utcStartDate = formmated_localStartDate - datetime.timedelta(hours=9)
formmated_utcEndDate = formmated_localEndDate - datetime.timedelta(hours=9)

# APIパラメータの指定
payload = {'units': 'm', 'format': 'csv'}
payload['apiKey'] = apiKey
backoff_period = 5

for index, row in locations.iterrows():
    url = 'https://api.weather.com/v3/wx/hod/conditions/historical/point?pointType=nearest&distance=50&geocode=' \
          + row['lat'] + ',' + row['lon']
    df = pd.DataFrame() #define empty dataframe

    for m in range(0, months, 1):

        #caluculate date
        calcStartDate = formmated_utcStartDate + relativedelta(months=m)
        calcEndDate = calcStartDate + relativedelta(months=1) - datetime.timedelta(hours=1)

        #convert to API parameter type(string)
        payload['startDateTime'] = calcStartDate.strftime("%Y%m%d%H%M")
        payload['endDateTime'] = calcEndDate.strftime("%Y%m%d%H%M")
        while True:
            try:
                response = requests.get(url, params=payload)
                if response.status_code == 200:
                    df1 = pd.read_csv(io.BytesIO(response.content), sep=",")
                    df = df.append(df1, ignore_index=True)
                    print(row['name'] + ': ' + str(calcStartDate) + '-' + str(calcEndDate) + '(UTC time) completed')
                    backoff_period = 5
                    break
                else:
                    print('Status code = {}'.format(response.status_code))
                    print('Point = {0}, startDateTime = {1}, endDateTime = {2}'.format(row['name'], payload['startDateTime'], payload['endDateTime']))
                    print('Sleep in {} secs'.format(backoff_period))
                    time.sleep(backoff_period)
                    backoff_period *= 2
                    if backoff_period >= 300:
                        backoff_period = 5
            except:
                print('Got an exception')
                print('Point = {0}, startDateTime = {1}, endDateTime = {2}'.format(row['name'], payload['startDateTime'], payload['endDateTime']))
                print('Sleep in {} secs'.format(backoff_period))
                time.sleep(backoff_period)
                backoff_period *= 5
                if backoff_period >= 300:
                    backoff_period = 5

    #重複行を削除
    df = df.drop_duplicates()

    df.to_csv("historicalData/" + row['name'] + '.csv', index = False)
    print(row['name'] + ": completed")