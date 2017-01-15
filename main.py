from travel_intelligence import travel_intelligence
from flight_calls import flight_calls
import CarRental
import current_location as cl

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
            print lst[0].fare
            if float(lst[0].fare)>self.budget:
                del_list.append(dest_list[i])
            new_list.append([dest_list[i],lst[0].fare])
        new_list=[[x,y] for x,y in new_list if x not in del_list]
        return new_list
m1=Main(1000,'2017-01-16','2017-01-18')
t1=travel_intelligence('Qpe6gVorrjycHAQGwUWQMkoL3012UOUA')
prev_year=int(m1.start[:4])-2
year_str=str(prev_year)+m1.start[4:7]
old_dest_list=t1.top_flight_destinations(year_str,m1.location)
new_dest_list=m1.get_feasible_flight(old_dest_list)






