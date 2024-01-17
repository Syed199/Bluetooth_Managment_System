from django.urls import path
from . import  views

app_name = 'faculty'

urlpatterns = [
    path('^$', views.home, name='home'),
    path('^regsuccess/$',views.regs,name='success'),
    path('^login/$',views.flogin,name='flogin'),
    path('^facultyhome/$',views.fachome,name='fachome'),
    path('^attendance/$',views.attendance,name='attendance'),
    path('^choosedate/$',views.sheet,name='sheet'),
    path('^editsheet/$',views.editsheet,name='editsheet'),
    path('^attendancesheet/$',views.viewsheet,name='viewsheet'),
    path('edit/$',views.view,name='view'),
    path('^logout/$',views.fac_logout,name='fac_logout'),
    path('^fullsheet/$', views.fullsheet, name='fullsheet')

]
