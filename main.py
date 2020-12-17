from loader import data_loader
from loader import weather_lookup

def run():
    source_df = data_loader.source_load(debug=False)
    #weather_lookup.generate_weather_data(source_df[['h_a','date','teamId']])

if __name__ == '__main__':
    run()