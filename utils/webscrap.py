import requests
from bs4 import BeautifulSoup
from utils.RandomForest import AQI_calculate

class webscrapping():
    def __init__(self,city):
        self.city=city


    def WebscrapData(self):
    
        url="https://en.tutiempo.net/"+self.city+".html?data=detailed"
        data=requests.get(url)
        code=data.content
        soup=BeautifulSoup(code,'html.parser')
        temp_max=((soup.find('td',class_="tiledia-1 first sel")).find('span',class_="t max")).text
        temp_min=((soup.find('td',class_="tiledia-1 first sel")).find('span',class_="t min")).text
        hum=((soup.find('div',class_="datadias detallado")).find('td',class_="first")).find_all('span',class_="hrd")
        maximum_temp=int(temp_max[:-1])
        minimum_temp=int(temp_min[:-1])
        average_temp=(maximum_temp+minimum_temp)/2
        humidity=int((str(hum[0]))[18:-8])
        windspeed=int((str(hum[2]))[18:-12])
        visibility=4.15
        suspended_windspeed=15.02
        inputdata=[[average_temp,maximum_temp,minimum_temp,humidity,visibility,windspeed,suspended_windspeed]]
        PM25=AQI_calculate(inputdata)
        DataDictionary={'Avg_temp':average_temp,'Max_temp':maximum_temp,'Min_temp':minimum_temp,'Humidity':humidity,'Visibility':visibility,'Wind_speed':windspeed,'Suspended_windspeed':suspended_windspeed,'PM25':PM25}
        return (DataDictionary)

