from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from pages.models import Section, Page
from mysite.functions import *
from django.utils.datastructures import MultiValueDictKeyError
 
def pageNav(request):
    section_list = Section.objects.all()
    for x in section_list:
        x.pages = Page.objects.filter(section = x.id)
        x.length = len(x.pages)
    return render(request, 'pagenav.html', {'sects': section_list})

	
def page_load(request, d, s, p):
    section = Section.objects.get(pk = s)
    page = Page.objects.get(pos = p, section = s)
    d.update({'s': s, 'p': p, 'section' : section, 'page': page, 'pageName' : ("s" + s + "p" + p)})
    return render(request, 'page.html', d)

def pageEdit(request, d, s, p):
    section = Section.objects.get(pk = s)
    page = Page.objects.get(pos = p, section = s)
    d.update({'s': s, 'p': p, 'section' : section, 'page': page, 'pageName' : ("s" + s + "p" + p)})
    return render(request, 'pageEdit.html', d)

def contentEdit(request, d, s, p):
    section = Section.objects.get(pk = s)
    page = Page.objects.get(pos = p, section = s)
    #request.encoding = 'utf-8'
    if request.method == 'POST':
        message = 'You entered: %r <br>' % str(request.POST['contentEditBox'])
        page.content = str(request.POST['contentEditBox'])
        page.name = str(request.POST['pageT'])
        page.save()
        section.name = str(request.POST['sectionT'])
        section.save()
        return HttpResponseRedirect('/pageEdit/%s/%s/' %(s, p))
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def pageDelete(request, d, s, p):
    section = Section.objects.get(pk = s)
    page = Page.objects.get(pos = p, section = s)
    if request.method == 'POST':
        try:
            del1 = str(request.POST['del1'])
        except MultiValueDictKeyError:
            del1 = False
        if del1 == 'on':
            message = delete(section, page)
        else:
            message='inactive'
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def structure(request, d):
    return render(request, 'structure.html', d)

def reOrder(request):
    if request.method == 'POST':
        arr = request.POST.getlist('array1[]')
        list = spOrder(arr)
        reOrderAction(list)
        message = 'success'
    else:
        message = 'nothing'
    return HttpResponse(message)