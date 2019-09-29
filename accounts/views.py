from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
import MySQLdb
import mysql.connector
from django import forms
from importlib import import_module
from django.conf import settings

# Create your views here.

'''def login(request):
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
          return render(request,'sign_in.html')  
          
def register(request):
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

def login(request):
    conn = mysql.connector.connect(user = 'root',password = 'root',host = 'localhost',database = 'trial')
    mycursor = conn.cursor()
    if request.method == 'POST':
        
        usrn = request.POST['usrname']
        pass1 = request.POST['pass']
        query="select usrname,prof,pswd1 from person"
        mycursor.execute(query)
        result=mycursor.fetchall()
        for res1 in result:
            if usrn in res1[0]:
                print("user accepted!")
                if pass1 in res1[1]:
                    print("Password accepted")
                    if prof == 'patient':
                        return redirect('/patient')
                    else:
                        return redirect('/doctor')

                    
                else:
                    print("Incorrect password")
            else:
                print("Incorrect user")

            '''
        query = 'insert into accounts_signin values(%s,%s)'
        args = (usrn,pass1)
        mycursor.execute(query,args)'''
        conn.commit()
        conn.close()
    
    return render(request,'sign_in.html') 

def d_next(request):
    conn = mysql.connector.connect(user = 'root',password = 'root',host = 'localhost',database = 'trial')
    mycursor = conn.cursor()
    if request.method == 'POST':
        lic_no = request.POST['lic_no']
        reg_no = request.POST['reg_no']
        experience = request.POST['exp']
        degree = request.POST['deg']
        spltion = request.POST['spltion']
        timing = request.POST['time']
        fee = request.POST['fee']
        pas1 = request.POST['pass1']
        pas2 = request.POST['pass2']
        user = request.session["usr"]
        query1 = 'insert into doctor(id,lic_no,reg_no,experience,degree,spltion,timing,fee) values ((select id from person where usrname="'+user+'"),"' + lic_no + '","' + reg_no + '","' + experience + '","' + degree +'","' + spltion +'","' + timing +'","' + fee +'")'
        query2 = "update person set pswd1 ='"+pas1+"',pswd2 = '"+pas2+"' where emailid = '" + request.session["email"] + "' "  
        
        mycursor.execute(query1,())
        mycursor.execute(query2,())
        conn.commit()
        conn.close()
        request.session["pswd"] = pas1
        return redirect('/')
    else:
        return render(request,'d_next.html') 

def p_next(request):
    conn = mysql.connector.connect(user = 'root',password = 'root',host = 'localhost',database = 'trial')
    mycursor = conn.cursor()
    if request.method == 'POST':
        wt = request.POST['wt']
        ht = request.POST['ht']
        med = request.POST['med']
        pas1 = request.POST['pass1']
        pas2 = request.POST['pass2']
        user = request.session["usr"]
        query1 = 'insert into patient(id,ht,wt,med_history) values ((select id from person where usrname="'+user+'"),"' + ht + '","' + wt + '","' + med + '")'
        query2 = "update person set pswd1 ='"+pas1+"',pswd2 = '"+pas2+"' where emailid = '" + request.session["email"] + "' "  
        
        mycursor.execute(query1,())
        mycursor.execute(query2,())
        conn.commit()
        conn.close()
        request.session["pswd"] = pas1
        return redirect('/')
    else:
        
        return render(request,'p_next.html') 
        
def register(request):
    conn = mysql.connector.connect(user = 'root',password = 'root',host = 'localhost',database = 'trial')
    mycursor = conn.cursor()
    if request.method == 'POST':
        prof = request.POST['profession']
        print(prof)
        usrname = request.POST['usrn']
        addr = request.POST['addr']
        emailid = request.POST['email']
        id_p = int(request.POST['id_proof'])
        gen = request.POST['gender']
        dob = request.POST['dob']
        phno = int(request.POST['phone'])

        query = 'insert into person(id,prof,usrname,addr,emailid,id_p,gender,dob,phno) values (id,"' + prof + '","' + usrname + '","' + addr + '","' + emailid + '",' + str(id_p) + ',"' + gen + '","'+ dob + '",' + str(phno)+')'
        mycursor.execute(query,())
        conn.commit()
        conn.close()
        request.session["email"] = emailid
        request.session["usr"] = usrname
        if prof == 'patient':
            return redirect('/p_next')
        else:
            return redirect('/d_next')
    else:
        return render(request,'index_reg.html')

def login_success(request):
    return render(request,'login_success.html')

'''def patient(request):
    return render(request,'patient.html')    
'''
def p_logout(request):
    logout(request)
    return redirect('/')

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def blog_home(request):
    return render(request,'blog-home.html')

def blog_single(request):
    return render(request,'blog-single.html')
