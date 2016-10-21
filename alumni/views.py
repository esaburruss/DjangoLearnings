from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render
from django.template import RequestContext
from mysite.functions import *
from alumni.models import Brother, Exec
from pages.models import Section, Page

def addAlumnus(request, d):
    PCs = pledgeClassList()
    Years = yearList(1988,2020)
    Months = monthList()
    execs = Exec.objects.all()
    states = stateList()
    d.update({'execs': execs, 'PCs': PCs, 'years': Years, 'months': Months, 'states': states})
    return render(request, 'addAlum.html', d)

def addAlumnusAction(request):
    if request.method == 'POST':
        message = 'success'
        phone = '(' + str(request.POST['phone1']) + ') ' + str(request.POST['phone2']) + '-' + str(request.POST['phone3'])
        brother = Brother(
            isApproved = 0,
            isAlumni = 1,
            firstName = str(request.POST['fName']),
            lastName = str(request.POST['lName']),
            nickName = str(request.POST['nName']),
            email = str(request.POST['email']),
            phone = phone,
            badge = str(request.POST['badge']),
            gradYear = str(request.POST['year']),
            state = str(request.POST['state']),
            city = str(request.POST['city']),
            zip = str(request.POST['zip']),
            streetAddress = str(request.POST['address']),
            pledgeClass = str(request.POST['pledge']),
            occupation = str(request.POST['occupation']),
            company = str(request.POST['company']),
            facebook = str(request.POST['facebook']),
            twitter = str(request.POST['twitter']),
            linkedIn = str(request.POST['linkedin']),
            website = str(request.POST['website']))
        brother.save()
        return HttpResponse(brother)
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)