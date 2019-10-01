from django.urls import path
from . import views
from django.conf.urls import url
import accounts.urls,accounts.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',views.doctor,name="doctor"),
    path('d_bill',views.d_bill,name="d_bill"),
    path('s_hours',views.s_hours,name="s_hours"),
    path('treat_list',views.treat_list,name="treat_list"),
    path('d_logout',views.d_logout,name="d_logout"),
]

