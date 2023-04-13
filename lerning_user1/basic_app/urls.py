from django.urls import re_path as url
from . import views

app_name = "basic_app"

urlpatterns = [
   
    url('user_login/',views.user_login,name='user_login'),
    url('go_login/',views.go_login,name='go_login'),
    url('home/',views.home,name='home'),
    url('logout/',views.user_logout,name='user_logout'),
]

