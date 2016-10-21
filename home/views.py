from django.template.loader import get_template
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from pages.models import Section, Page
#from pages.views import pageNav2
from mysite.functions import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request, d):
    return render(request, 'index.html', d)
    
def loginHandler(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            message = 'Logged in'
        else:
            message = 'Disabled User'
    else:
        message = 'Invalid User'
    return HttpResponse(message)

def dashboard(request, d):
    return render(request, 'dash.html', d)