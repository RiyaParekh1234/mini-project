from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    #path('index_reg/',views.register,name='register'),
    path('sign_in',views.login,name='sign_in'),
    path('logout',views.logout,name='logout'),
    path('',views.index,name='index'),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('blog-home',views.blog_home,name="blog-home"),
    path('blog-single',views.blog_single,name="blog-single"),
    path('login_success',views.login_success,name="log_success"),
    path('logout',views.p_logout,name="logout"),
]
urlpatterns += [
    url('index_reg',views.register,name="register"),
    url('p_next',views.p_next,name="p_next"),
    url('d_next',views.d_next,name="d_next"),
    url('s_hours',views.s_hours,name="s_hours"),
]
urlpatterns += staticfiles_urlpatterns()