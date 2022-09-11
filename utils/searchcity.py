import pandas as pd


def city_search(city):
    city=city
    df=pd.read_csv(r'C:\Users\Debasish\Desktop\Major Project\Project\AQI\utils\cityname.csv')
    city_list=list(df.City)
    if city in city_list:
        index=(city_list.index(city))
        City=(df['City Name'][index])

    return City











