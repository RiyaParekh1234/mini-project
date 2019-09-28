from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    #path('index_reg/',views.register,name='register'),
    path('sign_in',views.login,name='sign_in'),
    path('',views.index,name='index'),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('blog-home',views.blog_home,name="blog-home"),
    path('blog-single',views.blog_single,name="blog-single"),
    path('login_success',views.login_success,name="log_success"),
    #path('p_next',views.register,name="register")
    path('logout',views.p_logout,name="logout"),
    #path('patient',views.patient,name="patient")
]
urlpatterns += [
    url('index_reg',views.register,name="register"),
    url('p_next',views.p_next,name="p_next")
]
urlpatterns += staticfiles_urlpatterns()