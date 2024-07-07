from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
  path('',views.itachi_handler),
  path('register/',views.register_handler,name='register'),
  path('login/',views.login_handler,name='login'),
  path('logout/',views.logout_handler,name='logout'),
  path('vijay/',views.vijay_handler),
  path('vijay/haha',views.haha),
]