from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse('hello')
	
from urltest import Stay

def whoami(request):
	sex = request.GET['sex']
	name = request.GET['name']
	output_string = ""
	c1 = Stay()
	list = c1.getAirportHotelSearch()
	print list[0].address
	for index in range(len(list)):
		output_string += str(list[index].property_name)
		output_string += '\n'
		output_string += str(list[index].address)
		output_string += '\n'
		output_string += str(list[index].min_daily_amount)
		output_string += '\n'
		output_string += str(list[index].phone)
		output_string += '\n'
		output_string += str(list[index].fax)
		output_string += '\n'
		output_string += str(list[index].link)
		output_string += '\n'
		output_string += '\n'

	return HttpResponse(output_string, content_type="text/plain")

