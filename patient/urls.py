from django.urls import path
from . import views
from django.conf.urls import url
import accounts.urls,accounts.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',views.patient,name="patient"),
    path('appointment',views.appointment,name="appointment"),
    
    
]