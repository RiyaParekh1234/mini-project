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

def register(request):
    conn = mysql.connector.connect(user = 'root',password = 'root',host = 'localhost',database = 'trial')
    mycursor = conn.cursor()
    if request.method == 'POST':
        usrname = request.POST['usrn']
        addr = request.POST['addr']
        emailid = request.POST['email']
        id_p = int(request.POST['id_proof'])
        gen = request.POST['gender']
        dob = request.POST['dob']
        phno = int(request.POST['phno'])
        pswd1 = request.POST['pswd1']
        pswd2 = request.POST['pswd2']
        wh_hr = request.POST['wh_hr']
        sal = request.POST['sal']
        recep_type = request.POST['recep']

        query = 'insert into person(id,prof,usrname,addr,emailid,id_p,gender,dob,phno,pswd1,pswd2) values (id,"Receptionist","' + usrname + '","' + addr + '","' + emailid + '",' + str(id_p) + ',"' + gen + '","'+ dob + '",' + str(phno)+',"' + pswd1 + '","'+ pswd2 + '")'
        mycursor.execute(query,())
        query = 'insert into recept(id,r_salary,r_whrs,recep_name) values((select id from person where id_p='+str(id_p)+'),'+ str(sal) + ','+ str(wh_hr) +',"'+recep_type+'")'
        mycursor.execute(query,())
        conn.commit()
        conn.close()
        #equest.session["email"] = emailid
        #request.session["usr"] = usrname
        return render(request,'doctor.html')
    else:
        return render(request,'doctor/recep_reg.html') 

def r_next(request):
    return render(request,'doctor/r_next') 