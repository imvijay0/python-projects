
from  django.http import HttpResponse
from django.shortcuts import render 

def homepage(request):
  # return HttpResponse('Hi,i am home')
  return render(request,'home.html')

def aboutpage(request):
  # return HttpResponse('Hi i am about page')
  return render(request,'about.html')

def lolpage(request):
  return render(request,'lol.html')

  