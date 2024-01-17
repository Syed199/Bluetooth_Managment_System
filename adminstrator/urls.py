from django.urls import path 
from . import views

app_name = 'adminstrator'

urlpatterns = [
    path('$', views.home, name='home'),
    path('adminhome/$', views.adminhome, name='adminhome'),
    path('logoutadmin/$',views.logoutadmin,name='logoutadmin'),
    path('fapprove/$',views.fapproval,name='fapproval'),
    path('sapprove/$',views.sapproval,name='sapproval')
    ]