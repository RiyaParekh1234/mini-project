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

def patient(request):
    return render(request,'patient/patient.html')    

def appointment(request):
    conn = mysql.connector.connect(user = 'root',password = 'root',host = 'localhost',database = 'trial')
    mycursor = conn.cursor()
    if request.method == 'POST':
        usrname = request.POST['usrname']
        doctor = request.POST['doctor']
        gen = request.POST['gender']
        phno = request.POST['phno']
        emailid = request.POST['emailid']
        date = request.POST['date']
        time = request.POST['time']

        query1 = 'insert into appoint values (NULL,"' + usrname + '","' + doctor + '","' + gen + '","' + phno + '","' + emailid + '","' + date + '","' + time + '")'
        
        mycursor.execute(query1,())
        
        conn.commit()
        conn.close()
        
        return redirect('/')
    else:
       
        return render(request,'patient/appointment.html')


def bill(request):
    return render(request,'patient/bill.html')    


def p_logout(request):
    request.session.flush()
    return redirect('/')