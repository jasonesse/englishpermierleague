import pandas as pd
import requests

def get(debug=False):
    #resp = requests.get('https://www.wunderground.com/history/daily/EGGP/date/2019-8-9',timeout=(3.05, 27))
    resp = requests.get('https://api.weather.com/v1/location/EGGP:9:GB/observations/historical.json?apiKey=6532d6454b8aa370768e63d6ba5a832e&units=e&startDate=20190809&endDate=20190809')
    raw_json = resp.json()
    weather_data = raw_json['observations']
    weather_df = pd.DataFrame()
    for obs in weather_data:
        df = pd.DataFrame(data=obs, index=[0])
        weather_df = pd.concat([df, weather_df])
    
    if(debug):
        from explore.inspect import show_df
        show_df(weather_df)
    
    return weather_df