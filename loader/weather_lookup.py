import pandas as pd
import numpy as np
import requests
import datetime
from data.mapping.epl2020_stadiums import stadiums

def get_team_dates(df:pd.DataFrame):
    # get min/max date range
    teams_df = df.groupby(['teamId'])
    dates_df = teams_df['date'].agg([np.min, np.max])
    team_dates_df = pd.DataFrame(dates_df.to_records())
    team_dates_df.rename(columns={'amin':'min_date', 'amax': 'max_date'}, inplace=True)
    return team_dates_df

def get_date(date_str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

def get_str_date(date):
    return datetime.datetime.strftime(date,'%Y%m%d')

def generate_weather_data(df: pd.DataFrame):
    home_teams_df = df[df['h_a']=='h']
    #TODO get the rest of the stadium data... for now here's a sample
    home_teams_df = home_teams_df[home_teams_df['teamId'].isin(['Arsenal', 'Aston Villa', 'Bournemouth', 'Brighton', 'Burnley'])]
    team_dates_df = get_team_dates(home_teams_df)
    #for each stadium extract the weather data into files per month.
    for team_dates in team_dates_df.iterrows():
        team = team_dates[1]['teamId']
        weather_code = stadiums.get(team)[2] #weather code is in the array
        start = team_dates[1]['min_date']
        start_date = get_date(start)
        end = team_dates[1]['max_date']
        end_date = get_date(end)
        end_date = end_date.replace(month=4) #TODO hard coded for now.
        
        first_append = True
        for dt in pd.date_range(start=start_date, end=end_date, freq='M'):
            start_dt = dt.replace(day=1)
            stadium_df = get(weather_code=weather_code, start_date=get_str_date(start_dt), end_date=get_str_date(dt), debug=False)
            if first_append:
                #export headers once.
                stadium_df.to_csv(f'{team}.csv',columns=stadium_df.columns, index=False,mode='a')
                first_append = False
            else:
                stadium_df.to_csv(f'{team}.csv', index=False,mode='a')


        





def get(weather_code: str, start_date, end_date, debug=False):
    resp = requests.get(f'https://api.weather.com/v1/location/{weather_code}/observations/historical.json?apiKey=6532d6454b8aa370768e63d6ba5a832e&units=e&startDate={start_date}&endDate={end_date}')
    raw_json = resp.json()
    weather_data = raw_json['observations']
    observations = {}
    for obs in weather_data:
        observations.update({obs.get('valid_time_gmt'):obs})
        #observations.update({obs})
    #weather_df = pd.DataFrame(data=observations, index=[0])
    weather_df = pd.DataFrame.from_dict(observations, orient='index')
    weather_df['valid_time_gmt'] = pd.to_datetime(weather_df['valid_time_gmt'],unit='s')
    
    if(debug):
        from explore.inspect import show_df
        show_df(weather_df)
    
    return weather_df