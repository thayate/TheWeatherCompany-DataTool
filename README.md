# TheWeatherCompany-DataTool


## Overview
The Weather Companyが提供する、Weather Data Packageをより快適に使うためのツール
https://business.weather.com/products/weather-data-packages

Data Packageの名称ごとにディレクトリが分かれています。

## Description
[History-on-Demand/conditionsPull.py](https://github.com/thayate/TheWeatherCompany-DataTool/blob/master/History-on-Demand/conditionsPull.py)  
History on Demand - Conditions([仕様書](https://ibm.co/v3rHoDc))で複数拠点、長期間の過去データを取得するために使用します。

[Enhanced-Forecast/v3_FoDPull.py](https://github.com/thayate/TheWeatherCompany-DataTool/blob/master/Enhanced-Forecast/v3_FoDPull.py)  
Enhanced Forecast - 15-Day Hourly Forecast([仕様書](https://ibm.co/v3HFap))でデータを取得し、json -> csvにするために使用します。

## Dependency
ソースコードを実行するには、下記のソフトウェアが必要です。

- Python 3.x
- Pandas
- 該当Data PackageのAPI Key

Pandasを導入していない場合には下記のコマンドでインストールしてください。

`$ pip install pandas`

## Usage
各Data Packageのフォルダに移動して、Pythonコマンドを実行します。  
`    $ cd Enhanced-Forecast`
`    $ python v3_FoDPull.py`
