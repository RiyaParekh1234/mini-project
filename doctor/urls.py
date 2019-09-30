from django.urls import path
from . import views
from django.conf.urls import url
import accounts.urls,accounts.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',views.doctor,name="doctor"),
    path('d_bill',views.d_bill,name="d_bill"),
    
]

