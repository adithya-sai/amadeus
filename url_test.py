from amadeus import Hotels

class Stay:

	def Airport_Hotel_Search(self):
		final_result = {}
		property_name = []
		address = []
		amount = []
		phone = []
		fax = []
		link = []

		hotels = Hotels('Qpe6gVorrjycHAQGwUWQMkoL3012UOUA')
		resp = hotels.search_airport(location='BOS',check_in='2017-11-15',check_out='2017-11-16')
		for x in xrange(len(resp["results"])):
			final_result["property_name"] = property_name.append(resp["results"][x]["property_name"])
			final_result["address"] = address.append(resp["results"][x]["address"]["line1"] + ' ' + resp["results"][x]["address"]["city"] + ' ' + resp["results"][x]["address"]["region"] + ' ' + resp["results"][x]["address"]["postal_code"] + ' ' + resp["results"][x]["address"]["country"])
			final_result["min_daily_amount"] = amount.append(resp["results"][x]["total_price"]["currency"] + resp["results"][x]["total_price"]["amount"])
			final_result["phone"] = phone.append(resp["results"][x]["contacts"][0]["detail"])
			final_result["fax"] = fax.append(resp["results"][x]["contacts"][1]["detail"])
			final_result["link"] = link.append(resp["results"][x]["_links"]["more_rooms_at_this_hotel"]["href"])

		for key,value in final_result.items():
			print key, value


s = Stay()
s.Airport_Hotel_Search();