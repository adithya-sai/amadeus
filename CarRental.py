import urllib,json

class CarRental:
    def __init__(self):
        self.company_name = None

        self.airport_code = None

        self.address = None

        self.acriss_code = None

        self.transmission = None

        self.category = None

        self.type = None

        self.amount = None

        self.ratetype = None

        self.image = None

        self.image_width = None

        self.image_height = None

    def getCarRentalAirportSearch(self,locationandmoney,pick_up,drop_off):

        simplelist = []

        for k in range(len(locationandmoney)):
            api_url="https://api.sandbox.amadeus.com/v1.2/cars/search-airport?apikey="
            api_key="Qpe6gVorrjycHAQGwUWQMkoL3012UOUA"
            url=api_url+api_key+'&location='+locationandmoney[0][k]+'&pick_up='+pick_up+'&drop_off='+drop_off
            data=urllib.urlopen(url)
            resp=json.loads(data.read())
            min = -float('inf')
            for i in xrange(len(resp["results"])):
                # Need to write a for loop for cars
                # print(resp(['results'][x]['cars']))
                for j in range(len(resp['results'][i]['cars'])):
                    c = CarRental()

                    c.company_name = resp["results"][i]["provider"]["company_name"]

                    c.airport_code = resp["results"][i]["airport"]
                    if 'postal_code' not in resp["results"][i]["address"].keys():
                        c.address = resp["results"][i]["address"]["line1"] + ' ' + resp["results"][i]['address'][
                            'city'] + ' ' + resp["results"][i]["address"]["country"]
                    else:
                        c.address = resp["results"][i]["address"]["line1"] + ' ' + resp["results"][i]["address"][
                            "city"] + ' ' + \
                                    resp["results"][i]["address"]["postal_code"] + ' ' + resp["results"][i]["address"][
                                        "country"]

                    c.acriss_code = resp['results'][i]['cars'][j]['vehicle_info']['acriss_code']
                    c.transmission = resp['results'][i]['cars'][j]['vehicle_info']['transmission']
                    c.category = resp['results'][i]['cars'][j]['vehicle_info']['category']
                    c.type = resp['results'][i]['cars'][j]['vehicle_info']['type']
                    c.amount = 'USD ' + resp['results'][i]['cars'][j]['rates'][0]['price']['amount']
                    c.ratetype = resp['results'][i]['cars'][j]['rates'][0]['type']
                    if 'images' in resp['results'][i]['cars'][j].keys():
                        c.image = resp['results'][i]['cars'][j]['images'][0]['url']
                        c.image_width = resp['results'][i]['cars'][j]['images'][0]['width']
                        c.image_height = resp['results'][i]['cars'][j]['images'][0]['height']
                    #simplelist.append(c)

            return simplelist

#
# c1=CarRental()
# lst=(c1.getCarRentalAirportSearch('NCE','2017-01-15','2017-01-18'))

