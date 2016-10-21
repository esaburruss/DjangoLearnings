from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from .forms import UploadFileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from image.models import ImageUpload


def handle_uploads(request):
    file_name = ''
    direct = 'C:/Users/EXB8409/Documents/Django/mysite/static/img/'
    if request.user.is_authenticated():
        if request.method == 'POST':
            uploaded_file = request.FILES['myfile']
            file_name = uploaded_file.name
            # Write content of the file chunk by chunk in a local file (destination)
            with open(direct + file_name, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
        if(file_name != ''):
            imgURL = '/static/img/' + file_name
            img = ImageUpload.objects.create(name = file_name, url=imgURL, owner=request.user)
            img.save()
    response = HttpResponse('OK: ' + file_name)
    return response
    
def imgForm(request):
    return render(request, 'imgFormTest.html')