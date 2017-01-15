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
		if 'results' in  resp.keys():
			for i in xrange(len(resp["results"])):
				s = Stay()
				s.Airport_Hotel_Search(i,resp)
				simplelist.append(s)

		return simplelist

	def getSearchCircle(self,lat,long,ch_in,ch_out):

		simplelist = []
		hotels = Hotels('Qpe6gVorrjycHAQGwUWQMkoL3012UOUA')
		resp = hotels.search_airport(latitiude=lat,longitude=long,radius='42',check_in=ch_in,check_out=ch_out)
		if 'results' in resp.keys():
			for i in xrange(len(resp["results"])):
				s = Stay()
				s.Airport_Hotel_Search(i,resp)
				simplelist.append(s)

		return simplelist

	def Airport_Hotel_Search(self,x,resp):

		if 'property_name' in resp.keys():
			self.property_name = resp["results"][x]["property_name"]
		if 'address' in resp.keys():
			self.address = resp["results"][x]["address"]["line1"] + ' ' + resp["results"][x]["address"]["city"] + ' ' + resp["results"][x]["address"]["region"] + ' ' + resp["results"][x]["address"]["postal_code"] + ' ' + resp["results"][x]["address"]["country"]
		if 'min_daily_amount' in resp.keys():
			self.min_daily_amount = resp["results"][x]["total_price"]["currency"] + resp["results"][x]["total_price"]["amount"]
		if 'contacts' in resp.keys():	
			self.phone = resp["results"][x]["contacts"][0]["detail"]
			self.fax = resp["results"][x]["contacts"][1]["detail"]
		if 'descriptions' in resp.keys():
			self.description = resp["results"][x]["descriptions"]
		if 'room_type_info' in resp.keys():
			self.room_type = resp["results"][x]["room_type_info"]["room_type"]
			self.bed_type = resp["results"][x]["room_type_info"]["bed_type"]
			self.number_of_beds = resp["results"][x]["room_type_info"]["number_of_beds"]
		if '_links' in resp.keys():
			self.link = resp["results"][x]["_links"]["more_rooms_at_this_hotel"]["href"]


s = Stay()
print s.getAirportHotelSearch('BOS','2017-01-16','2017-01-19')

