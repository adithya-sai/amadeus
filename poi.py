import urllib,json
import collections

class points:
    def __init__(self,api_key):
        self.api_key=api_key

    def points_list(self,city,duration):
        api_url = 'https://api.sandbox.amadeus.com/v1.2/points-of-interest/yapq-search-text?apikey='
        url=api_url+self.api_key+'&city_name='+city.replace(' ','%20')
        resp=urllib.urlopen(url)
        data=json.loads(resp.read())
        list= collections.OrderedDict()
        for i in range(duration):
            list[data['points_of_interest'][i]['title']] = float(data['points_of_interest'][i]['grades']['yapq_grade'])
        return list
    def points_values(self,list):
        sum = 0
        for i in list.keys():
            sum += list[i]
        avg = float(sum/len(list))
        return avg
p = points('Qpe6gVorrjycHAQGwUWQMkoL3012UOUA')
list = p.points_list('Las Vegas',5)
print list
values = p.points_values(list)
print values
