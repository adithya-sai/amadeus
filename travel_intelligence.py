import urllib,json

class travel_intelligence:
    def __init__(self,api_key):
        self.api_key=api_key
    def top_flight_destinations(self,period,origin):
        api_url = 'https://api.sandbox.amadeus.com/v1.2/travel-intelligence/top-destinations?apikey='
        url=api_url+self.api_key+'&period='+period+'&origin='+origin
        resp=urllib.urlopen(url)
        data=json.loads(resp.read())
        dest_list=[]
        for i in range(len(data['results'])):
            dest_list.append(str(data['results'][i]['destination']))
        return dest_list
    def top_flight_search(self,period,origin,country,destination=None):
        api_url='https://api.sandbox.amadeus.com/v1.2/travel-intelligence/top-searches?apikey='
        if(destination!=None):
            url=api_url+self.api_key+'&period='+period+'&origin='+origin+'&destination='+destination+'&country='+country
        else:
            url=api_url+self.api_key+'&period='+period+'&origin='+origin+'&country='+country
        resp=urllib.urlopen(url)
        data=json.loads(resp.read())
        dest_list=[]
        for i in range(len(data['results'])):
            dest_list.append(str(data['results'][i]['destination']))
        return dest_list
t1=travel_intelligence('Qpe6gVorrjycHAQGwUWQMkoL3012UOUA')
print(t1.top_flight_destinations('2015-09','BOS'))
print(t1.top_flight_search('2015-09','BOS','US'))





