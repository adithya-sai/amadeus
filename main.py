from travel_intelligence import travel_intelligence
from flight_calls import flight_calls
from CarRental import CarRental
import current_location as cl
from Stay import Stay

iata={'Los Angeles':'LAX', 'Tucson':'TUS', 'Las Vegas':'LAS', 'Denver':'DEN','Chicago':'CHI','San Deigo':'SAN','Seattle':'SEA','Dallas':'DFW','New York':'NYC','San Francisco':'SFO','Phoenix':'PHX'}

class Main:
    def __init__(self,budget,start,end):
        self.budget=budget
        self.start=start
        self.end=end
        self.location=iata[cl.get_location()]

    def get_feasible_flight(self,dest_list):
        del_list=[]
        new_list = []
        flight_cost = flight_calls('Qpe6gVorrjycHAQGwUWQMkoL3012UOUA')
        for i in range(len(dest_list)):
            lst=flight_cost.flight_low_fare_search(self.location,dest_list[i],self.start)
            if float(lst[0].fare)>self.budget:
                del_list.append(dest_list[i])
            new_list.append([dest_list[i],lst[0].fare])
        new_list=[[x,y] for x,y in new_list if x not in del_list]
        return new_list

    def get_feasible_hotel(self,dest_list):
        new_list=[]
        hotel=Stay()
        for i in xrange(len(dest_list)):
            print dest_list[i][0]
            temp=hotel.getAirportHotelSearch(dest_list[i][0],'2017-01-16','2017-01-18')
            print temp
            new_list.append([dest_list[i][0],temp[0].min_daily_amount])
        return new_list



    
m1=Main(1000,'2017-01-16','2017-01-18')
t1=travel_intelligence('Qpe6gVorrjycHAQGwUWQMkoL3012UOUA')
prev_year=int(m1.start[:4])-2
year_str=str(prev_year)+m1.start[4:7]
old_dest_list=t1.top_flight_destinations(year_str,m1.location)
new_dest_list_flight=m1.get_feasible_flight(old_dest_list)

print new_dest_list_flight


c = CarRental()
car_rental_dist = []
for i in range(len(new_dest_list_flight)):
        carrentals = c.getCarRentalAirportSearch(new_dest_list_flight[i][0],'2017-01-16','2017-01-19')
        min = float('inf')
        loc = None
        count = 0
        if carrentals:
            for carrental in carrentals:
                if carrental.amount:
                    if float(carrental.amount[3:]) < min:
                        min = float(carrental.amount[3:])
                        loc = new_dest_list_flight[i][0]
                        count += 1
        if count > 0:              
            car_rental_dist.append([loc,min])

print car_rental_dist

s = Stay()
hotel_rental_dist = []
for i in range(len(new_dest_list_flight)):
        hotels = s.getAirportHotelSearch(new_dest_list_flight[i][0],'2017-01-16','2017-01-19')   
        minimum = float('inf')
        loc = None
        count = 0
        if hotels:
            for hotel in hotels:
                if hotel.min_daily_amount:
                    if float(hotel.min_daily_amount[3:]) < minimum:
                        minimum = float(hotel.min_daily_amount[3:])
                        loc = new_dest_list_flight[i][0]
                        count += 1
        if count > 0:                
            hotel_rental_dist.append([loc,minimum])

print hotel_rental_dist


new_flight=flight_calls('Qpe6gVorrjycHAQGwUWQMkoL3012UOUA')
flight_info=new_flight.flight_low_fare_search(m1.location,new_dest_list_flight[0][0],m1.start)

new_hotel=Stay()
hotel_info=new_hotel.getAirportHotelSearch(new_dest_list_flight[0][0],m1.start,m1.end)

new_car=CarRental()
car_info=new_car.getCarRentalAirportSearch(new_dest_list_flight[0][0],m1.start,m1.end)





