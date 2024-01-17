from django.urls import include ,path
from django.contrib import admin
from . import  views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('adminstrator/',include('adminstrator.urls')),
    path('faculty/',include('faculty.urls')),
    path('student/',include('student.urls')),
]
