from django.shortcuts import render,redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def posts_list(request):
  posts = Post.objects.all().order_by('-date')
  return render(request,'posts/posts_list.html',{'posts':posts})

def post_page(request,slug):
  post = Post.objects.get(slug=slug)
  return render(request,'posts/post_page.html',{'post':post})

# if user is not logged in ,take him to login page
@login_required(login_url="/users/login/")
def new_post_hanlder(request):
  if request.method == 'POST':
    form = forms.CreatePost(request.POST,request.FILES)
    if form.is_valid:
      newpost = form.save(commit=False)
      newpost.author = request.user
      newpost.save()
      return redirect('posts:list')
  else:
    form = forms.CreatePost()
  return render(request,'posts/new_post.html',{'form':form})