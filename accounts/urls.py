from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('index_reg/',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('',views.index,name='index'),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('blog-home',views.blog_home,name="blog_home"),
    path('blog-single',views.blog_single,name="blog_single"),
    path('login_success',views.log_success,name="log_success"),
]
urlpatterns += staticfiles_urlpatterns()