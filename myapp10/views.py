from django.shortcuts import render
from django.http import HttpResponse
from .functions import handle_uploaded_file
from .forms import Studentform

def index(request):
    if request.method == 'POST':
        student = Studentform(request.POST, request.FILES)#passing as parameter
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("file uploaded successfully")
    else:
        student = Studentform()
        return render(request, "index.html", {'form': student})


# Create your views here.
