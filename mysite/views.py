from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from mysite.functions import *

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def current_datetime2(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def hello(request):
	return HttpResponse("Hello world")
	
def test(request):
    if request.method == 'POST':
        arr = request.POST.getlist('array1[]')
        list = spOrder(arr)
        reOrder(list)
        message = 'success'
    else:
        message = 'nothing'
    return HttpResponse(message)