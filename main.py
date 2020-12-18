from loader import source_loader
from loader import weather_loader

def preprocess_data():
    source_df = source_loader.load(debug=False)
    weather_df = weather_loader.load(df=source_df, generate=False)
    #
    #join up weather data to source_df. 
    

if __name__ == '__main__':
    preprocess_data()