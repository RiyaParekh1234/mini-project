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

def doctor(request):
    return render(request,'doctor.html')   

def d_bill(request):
    conn = mysql.connector.connect(user = 'root',password = 'root',host = 'localhost',database = 'trial')
    mycursor = conn.cursor()
    if request.method == 'POST':
        pusr = request.POST['usrname']
        diag = request.POST['diag']
        usrn = request.session["user"]	                   
        query1 = "insert into bill(id,doc_name,bill_dt,diag) values ((select id from person where usrname='"+pusr+"'),'"+ str(usrn) +"',(select CURDATE()),'"+ diag +"')"        
        mycursor.execute(query1,())
        conn.commit()
        conn.close()
        return redirect('/doctor')
    
    return render(request,'doctor/u_bill.html')     

def s_hours(request):
    conn = mysql.connector.connect(user = 'root',password = 'root',host = 'localhost',database = 'trial')
    mycursor = conn.cursor()
    if request.method == 'POST':
        query="select usrname from person p,doctor d where p.id=d.id"
        mycursor.execute(query)
        result=mycursor.fetchone()
        newtime = request.POST['time']
        query1 = "update doctor set timing = '"+ newtime +"' where id=(select id from person where usrname='"+ result[0] +"')"
        mycursor.execute(query1,())
        conn.commit()
        conn.close()
        return redirect('/doctor')
    else:
        return render(request,'doctor/s_hours.html')


def treat_list(request):
    conn = mysql.connector.connect(user = 'root',password = 'root',host = 'localhost',database = 'trial')
    mycursor = conn.cursor()
    usrn = request.session["user"]
    u_id = request.session["uid"]
    #query1 = "select * from patient "
    query2 = "select p.id,d.usrname,d.emailid,d.phno,p.ht,p.wt,p.med_history from person d,patient p where p.id=d.id "
    #mycursor.execute(query1,())
    #res1=mycursor.fetchall()
    mycursor.execute(query2,())    
    res2=mycursor.fetchall()
    conn.commit()
    conn.close() 
    return render(request,'doctor/treat_list.html',{'res2':res2})     

def d_logout(request):
    request.session.flush()
    return redirect('/')

