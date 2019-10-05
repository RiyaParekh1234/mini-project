from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
import MySQLdb
import mysql.connector
from django import forms
from importlib import import_module
from django.conf import settings
<<<<<<< HEAD
=======


>>>>>>> 3807c72fe443d8e481b5e60fc2508cf93d3668ff

# Create your views here.

def doctor(request):
<<<<<<< HEAD
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
=======
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

>>>>>>> 3807c72fe443d8e481b5e60fc2508cf93d3668ff
