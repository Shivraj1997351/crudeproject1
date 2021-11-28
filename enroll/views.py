from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import StudentRegistration
from enroll.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
# Create your views here.

#add data 
def add_show(request):
 if request.method == 'POST':
  fm = StudentRegistration(request.POST)
  if fm.is_valid():
   nm = fm.cleaned_data['name']
   em = fm.cleaned_data['email']
   pwd = fm.cleaned_data['password']
   pw = make_password(pwd)
   reg = User(name=nm,email=em,password=pw)
   reg.save()
   fm = StudentRegistration()
   messages.add_message(request, messages.SUCCESS, 'New Record inserted')
 else:
  fm = StudentRegistration()
 stud = User.objects.all()
  
 return render(request, 'enroll/addandshow.html', {'form':fm,'stu':stud})

#update data
def update_data(request, id):
 if request.method == 'POST':
  pi = User.objects.get(pk=id)
  fm = StudentRegistration(request.POST,instance=pi)
  if fm.is_valid():
   fm.save()
   messages.add_message(request, messages.INFO, 'Record updated')
 else:
   pi = User.objects.get(pk=id)
   fm = StudentRegistration(instance=pi)
 return render(request, 'enroll/updatestudent.html', {'form':fm})
    
#delete data
def delete_data(request, id):
 if request.method == 'POST':
  pi = User.objects.get(pk=id)
  pi.delete()
  messages.add_message(request, messages.INFO, 'Record deleted')
  return HttpResponseRedirect('/')

#delete all data
def delete_alldata(request):
 if request.method == 'POST':
  pi = User.objects.all()
  pi.delete()
  messages.add_message(request, messages.INFO, 'All Records deleted')
  return HttpResponseRedirect('/')
  