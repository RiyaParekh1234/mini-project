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