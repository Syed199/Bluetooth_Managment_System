from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('$', views.home, name='home'),
    path('regsuccess/$', views.regs, name='success'),
    path('login/$',views.slogin,name='slogin'),
    path('studenthome/$',views.shome,name='shome'),
    path('logout/$',views.stud_logout,name='stud_logout'),
    path('forgotpassword/$',views.fpass,name='fpass'),
    path('emailsent/$',views.email,name='email')
]
