from amadeus import Flights
class flight_calls:

    def __init__(self,api_key):
        self.api_key=api_key
        self.flight_number=None
        self.flight_departure=None
        self.flight_arrival = None
        self.origin=None
        self.destination=None
        self.flight_class=None
        self.fare=None


    # def flight_inspiration_search(self,origin,destination=None,departure_date=None,one_way=None,duration=None,direct=None,max_price=None,aggregation_mode=None):
    #     flights = Flights(self.api_key)
    #     resp=flights.inspiration_search(origin=origin,destination=destination,one_way=one_way,duration=duration,direct=direct,max_price=max_price,aggregation_mode=aggregation_mode)
    #     return resp
    # def flight_extensive_search(self,origin,destination,departure_date=None,one_way=None,duration=None,direct=None,max_price=None,aggregation_mode=None):
    #     flights = Flights(self.api_key)
    #     resp=flights.extensive_search(origin=origin,destination=destination,departure_date=None,one_way=None,duration=None,direct=None,max_price=None,aggregation_mode=None)
    #     return resp
    #


    def flight_low_fare_search(self,origin,destination,departure_date,return_date=None,arrive_by=None,return_by=None,adults=None,children=None,infants=None):
        flights = Flights(self.api_key)
        flight_list=[]
        resp=flights.low_fare_search(origin=origin,destination=destination,departure_date=departure_date,return_date=return_date,arrive_by=arrive_by,return_by=return_by,adults=adults,children=children,infants=infants)
        for i in xrange(len(resp['results'])):
            new_flight = flight_calls('Qpe6gVorrjycHAQGwUWQMkoL3012UOUA')
            new_flight.flight_details(i,resp)
            flight_list.append(new_flight)
        return flight_list
        # flight_info=[]
        # for i in range(len(resp['results'])):
        #     for j in range(len(resp['results'][i]['itineraries'])):
        #         # resp['results'][i]['itineraries'][j]['outbound']['flights']['fare']=resp['results'][i]['fare']['total_price']
        #         flight_info.append(resp['results'][i]['itineraries'][j]['outbound']['flights'])
        # return flight_info

    def flight_details(self,i,resp):
        for j in xrange(len(resp['results'][i]['itineraries'])):
            for k in xrange(len(resp['results'][i]['itineraries'][j]['outbound']['flights'])):
                self.flight_number=resp['results'][i]['itineraries'][j]['outbound']['flights'][k]['flight_number']
                self.flight_departure = resp['results'][i]['itineraries'][j]['outbound']['flights'][k]['departs_at']
                self.flight_arrival = resp['results'][i]['itineraries'][j]['outbound']['flights'][k]['arrives_at']
                self.origin = str(resp['results'][i]['itineraries'][j]['outbound']['flights'][k]['origin']['airport'])#+' - Terminal '+str(resp['results'][i]['itineraries'][j]['outbound']['flights'][k]['origin']['terminal'])
                self.destination = str(resp['results'][i]['itineraries'][j]['outbound']['flights'][k]['destination']['airport'])#+' - Terminal '+str(resp['results'][i]['itineraries'][j]['outbound']['flights'][k]['destination']['terminal'])
                self.flight_arrival = resp['results'][i]['itineraries'][j]['outbound']['flights'][k]['booking_info']['travel_class']
                self.fare=resp['results'][i]['fare']['total_price']


# flight number, departs at, arrives at, airport, terminal,destination,
f1=flight_calls('Qpe6gVorrjycHAQGwUWQMkoL3012UOUA')
# lst=(f1.flight_low_fare_search('NYC','BOS','2017-01-14'))
# print(lst[0].flight_number)
