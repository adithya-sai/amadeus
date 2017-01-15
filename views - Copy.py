from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse('hello')
	
from validate import val

def whoami(request):


	
    sex = request.GET['sex']
    name = request.GET['name']

    return HttpResponse(val(sex,name))

