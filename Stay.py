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
		if "results" in  resp.keys():
			for i in xrange(len(resp["results"])):
				s = Stay()
				s.property_name = resp["results"][i]["property_name"]
				s.address = resp["results"][i]["address"]["line1"] + ' ' + resp["results"][i]["address"]["city"] + ' ' + resp["results"][i]["address"]["region"] + ' ' + resp["results"][i]["address"]["postal_code"] + ' ' + resp["results"][i]["address"]["country"]
				s.min_daily_amount = resp["results"][i]["total_price"]["currency"] + resp["results"][i]["total_price"]["amount"]	
				s.phone = resp["results"][i]["contacts"][0]["detail"]
				s.fax = resp["results"][i]["contacts"][1]["detail"]
				if "descriptions" in resp.keys():
					s.description = resp["results"][i]["descriptions"]
				if "room_type" in resp.keys():
					s.room_type = resp["results"][i]["room_type_info"]["room_type"]
					s.bed_type = resp["results"][i]["room_type_info"]["bed_type"]
					s.number_of_beds = resp["results"][i]["room_type_info"]["number_of_beds"]
				s.link = resp["results"][i]["_links"]["more_rooms_at_this_hotel"]["href"]
				simplelist.append(s)

		return simplelist

	def getSearchCircle(self,lat,longi,ch_in,ch_out):

		simplelist = []
		hotels = Hotels('Qpe6gVorrjycHAQGwUWQMkoL3012UOUA')
		resp = hotels.search_airport(latitiude=lat,longitude=longi,radius='42',check_in=ch_in,check_out=ch_out)
		if 'results' in resp.keys():
			for i in xrange(len(resp["results"])):
				s = Stay()
				s.property_name = resp["results"][i]["property_name"]
				s.address = resp["results"][i]["address"]["line1"] + ' ' + resp["results"][i]["address"]["city"] + ' ' + resp["results"][i]["address"]["region"] + ' ' + resp["results"][i]["address"]["postal_code"] + ' ' + resp["results"][i]["address"]["country"]
				s.min_daily_amount = resp["results"][i]["total_price"]["currency"] + resp["results"][i]["total_price"]["amount"]	
				s.phone = resp["results"][i]["contacts"][0]["detail"]
				s.fax = resp["results"][i]["contacts"][1]["detail"]
				if "descriptions" in resp.keys():
					s.description = resp["results"][i]["descriptions"]
				if "room_type" in resp.keys():
					s.room_type = resp["results"][i]["room_type_info"]["room_type"]
					s.bed_type = resp["results"][i]["room_type_info"]["bed_type"]
					s.number_of_beds = resp["results"][i]["room_type_info"]["number_of_beds"]
				s.link = resp["results"][i]["_links"]["more_rooms_at_this_hotel"]["href"]
				simplelist.append(s)

		return simplelist

		

