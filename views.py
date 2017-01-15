from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse('hello')
	
from urltest import Stay

from django.views.generic.base import TemplateView

from CarRental import CarRental
	
from travel_intelligence import travel_intelligence
from django.http import HttpResponse
from django.shortcuts import render_to_response	
class HomeView(TemplateView):

    template_name = 'index.html'


def hotels(request):
	
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
		
		hotel_string = output_string
		
	c1 = travel_intelligence('Qpe6gVorrjycHAQGwUWQMkoL3012UOUA')
	top_flight = ""
	list1 = c1.top_flight_destinations('2015-09','BOS')
	for index in range(len(list1)):
		top_flight += list1[index]
		top_flight += '\n'
		top_flight += '\n'
	


	return render_to_response('resultbase.html', context = {
      'hotel': hotel_string,
	  'flight': top_flight,
    })
	



	
def flights(request):
	output_string = ""
	c1 = travel_intelligence('Qpe6gVorrjycHAQGwUWQMkoL3012UOUA')
	
	list = c1.top_flight_destinations('2015-09','BOS')
	for index in range(len(list)):
		output_string += list[index]
		output_string += '\n'
		
	render_to_response('index.html', {'name': output_string})

from django.shortcuts import render_to_response
def some_view(request):
	return render_to_response('index.html', context = {
      'name': 'naren',
    })