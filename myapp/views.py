from django.shortcuts import render
from myapp.forms import *
from myapp.models import *
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
        print("post request")
        form = EmployeeForm(request.POST)
        if form.is_valid():
            print("data validated")
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            data = Employee(name=nm, email=em)
            data.save()
            messages.success(request,'employee data submitted !!')
    else:
        print("get request")
        form = EmployeeForm()
    return render(request,'index.html',locals())