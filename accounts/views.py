from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
import MySQLdb
import mysql.connector
# Create your views here.

def login(request):
    if request.method == 'POST':
        usr = request.POST['usrname']
        pass1 = request.POST['pass']
        user = auth.authenticate(username=usr,password=pass1)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print("Invalid credentials")    
    else:
          return render(request,'login_page.html')  
          
'''def register(request):
    if request.method == 'POST':
        usr = request.POST['usrname']
        pass1 = request.POST['pass']
        pass2 = request.POST['cpass']
        mailID = request.POST['mailId']

        if pass1==pass2:
            if User.objects.filter(username=usr).exists():
                print("Username taken")
            elif User.objects.filter(email=mailID).exists():
                print("Email taken")
            else:
                user = User.objects.create_user(username=usr,password=pass1,email=mailID)
                user.save()
                print("User created!")
                return redirect('/')
        else:
            print("Password not matching!")
    else:    
        return render(request,'index_reg.html')'''

def register(request):
    conn = mysql.connector.connect(user = 'root',password = 'shreya00',host = 'localhost',database = 'trial')
    mycursor = conn.cursor()
    if request.method == 'POST':
        usr = request.POST['username']
        emailid = request.POST['email']
        phno = request.POST['phone']

        query = 'insert into accounts_registration values(105,%s,%s,%s)'
        args = (usr,emailid,phno)
        mycursor.execute(query,args)
        conn.commit()
    else:
        return render(request,'index_reg.html') 

def log_success(request):
    return redirect('login_success.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def blog_home(request):
    return render(request,'blog_home.html')

def blog_single(request):
    return render(request,'blog_single.html')