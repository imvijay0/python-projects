from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.
def itachi_handler(request):
  return HttpResponse('hi sasuke')

def vijay_handler(request):
  return HttpResponse('my name is vijay')

def haha(request):
  return HttpResponse('hahahahaha')

def register_handler(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      login(request,form.save())
      return redirect("posts:list")
  else:
    form = UserCreationForm()
  return render(request,'users/register.html',{'form':form})

def login_handler(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      login(request,form.get_user()) # log the user immediately
      if "next" in request.POST:
        # in the next parameter we have url like next=posts/new-post
        return redirect(request.POST.get('next')) 
      return redirect('posts:list')
      
  else: # if it's just a get request
    form = AuthenticationForm()
  return render(request,'users/login.html',{'form':form})

def logout_handler(request):
  if request.method == 'POST':
    logout(request)
    return redirect('posts:list')