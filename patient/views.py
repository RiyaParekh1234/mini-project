from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
import MySQLdb
import mysql.connector
from django import forms
from importlib import import_module
from django.conf import settings
from accounts.views import login
import getpass


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
    conn = mysql.connector.connect(user = 'root',password = 'root',host = 'localhost',database = 'trial')
    mycursor = conn.cursor()
    '''
    query1 = "select usrname from person where status='T'"
    query2 = "select phno from person where status='T'"
    query3 = "select emailid from person where status='T'"
    mycursor.execute(query1,())
    res1=mycursor.fetchall()
    mycursor.execute(query2,())
    res2=mycursor.fetchall()
    mycursor.execute(query3,())
    res3=mycursor.fetchall()
    '''
    usrn = request.session["user"]
    u_id = request.session["uid"]
    query1 = "select phno,emailid from person where usrname = '" + request.session["user"] + "'"
    query2 = "select * from bill where id = '" + str(u_id) + "' "
    mycursor.execute(query1,())
    res1=mycursor.fetchall()

    mycursor.execute(query2,())
    res2=mycursor.fetchall()
    
    conn.commit()
    conn.close()
    return render(request,'patient/bill.html',{'usrname':usrn,'phno': res1[0][0],'emailid': res1[0][1],'date':res2[0][3],'bill_id':res2[0][0],'doc':res2[0][2],'diag':res2[0][4],'amt':res2[0][5],'tot':res2[0][7]})    


def p_logout(request):
    conn = mysql.connector.connect(user = 'root',password = 'root',host = 'localhost',database = 'trial')
    mycursor = conn.cursor()
    query1="update person set status='F' where status='T' "
    mycursor.execute(query1,())
    conn.commit()
    conn.close()
    request.session.flush()
    return redirect('/')