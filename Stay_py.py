from amadeus import Hotels

class Stay:

	def __init__(self):

		self.property_name = None
		self.address = None
		self.min_daily_amount = None
		self.phone = None
		self.fax = None
		self.description = None
		self.room_type = None
		self.bed_type = None
		self.number_of_beds = None
		self.link = None

	def getAirportHotelSearch(self,loc,ch_in,ch_out):
		
		simplelist = []
		hotels = Hotels('Qpe6gVorrjycHAQGwUWQMkoL3012UOUA')
		resp = hotels.search_airport(location=loc,check_in=ch_in,check_out=ch_out)
		for i in xrange(len(resp["results"])):
			s = Stay()
			s.Airport_Hotel_Search(i,resp)
			simplelist.append(s)

		return simplelist

	def getSearchCircle(self,lat,longe,rad,ch_in,ch_out):

		simplelist = []
		hotels = Hotels('Qpe6gVorrjycHAQGwUWQMkoL3012UOUA')
		resp = hotels.search_airport(latitiude=lat,longitude=longe,radius=rad,check_in=ch_in,check_out=ch_out)
		for i in xrange(len(resp["results"])):
			s = Stay()
			s.Airport_Hotel_Search(i,resp)
			simplelist.append(s)

		return simplelist

	def Airport_Hotel_Search(self,x,resp):

		self.property_name = resp["results"][x]["property_name"]
		self.address = resp["results"][x]["address"]["line1"] + ' ' + resp["results"][x]["address"]["city"] + ' ' + resp["results"][x]["address"]["region"] + ' ' + resp["results"][x]["address"]["postal_code"] + ' ' + resp["results"][x]["address"]["country"]
		self.min_daily_amount = resp["results"][x]["total_price"]["currency"] + resp["results"][x]["total_price"]["amount"]
		self.phone = resp["results"][x]["contacts"][0]["detail"]
		self.fax = resp["results"][x]["contacts"][1]["detail"]
		self.description = resp["results"][x]["descriptions"]
		self.room_type = resp["results"][x]["room_type_info"]["room_type"]
		self.bed_type = resp["results"][x]["room_type_info"]["bed_type"]
		self.number_of_beds = resp["results"][x]["room_type_info"]["number_of_beds"]
		self.link = resp["results"][x]["_links"]["more_rooms_at_this_hotel"]["href"]

