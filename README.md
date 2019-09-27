# TheWeatherCompany-DataTool


## Overview
The Weather Companyが提供する、Weather Data Packageをより快適に使うためのツール
https://business.weather.com/products/weather-data-packages

Data Packageの名称ごとにディレクトリが分かれています。

## Dependency
ソースコードを実行するには、下記のソフトウェアが必要です。

- Python 3.x
- Pandas
- 該当Data PackageのAPI Key

Pandasを導入していない場合には下記のコマンドでインストールしてください。

`$ pip install pandas`

## Usage
各Data Packageのフォルダに移動して、Pythonコマンドを実行します。  
`$ cd Enhanced-Forecast`  
`$ python v3_FoDPull.py`

## Description
[History-on-Demand/conditionsPull.py](https://github.com/thayate/TheWeatherCompany-DataTool/blob/master/History-on-Demand/conditionsPull.py)  
History on Demand - Conditions([仕様書](https://ibm.co/v3rHoDc))で複数拠点、長期間の過去データを取得するために使用します。
実行すると、API Keyと取得期間の入力が求められ、[pointList.csv](https://github.com/thayate/TheWeatherCompany-DataTool/blob/master/History-on-Demand/pointList.csv)にある地点のデータが取得されます。

[Enhanced-Forecast/v3_FoDPull.py](https://github.com/thayate/TheWeatherCompany-DataTool/blob/master/Enhanced-Forecast/v3_FoDPull.py)  
Enhanced Forecast - 15-Day Hourly Forecast([仕様書](https://ibm.co/v3HFap))でデータを取得し、json -> csvにするために使用します。
コードに取得したいポイントの緯度経度とAPI Keyを直接[v3_FoDPull.py](https://github.com/thayate/TheWeatherCompany-DataTool/blob/master/Enhanced-Forecast/v3_FoDPull.py)に書き込んでご利用ください。

## License
本リポジトリのソースコードはMITライセンスです。 商用・非商用問わず、自由にご利用ください。
