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

def bill_final(request):
    conn = mysql.connector.connect(user = 'root',password = 'root',host = 'localhost',database = 'trial')
    mycursor = conn.cursor()
    if request.method == 'POST':
        usrname = request.POST['usrname']
        b_amt = request.POST['b_amt']
        query1 = 'select id from person where usrname="'+usrname+'" and prof="Patient"'
        mycursor.execute(query1)
        h_id = mycursor.fetchone()
        query = "update bill set amt='"+b_amt+"' where id = '"+ str(h_id[0])+"' "
        mycursor.execute(query)

        conn.commit()
        conn.close()
        return redirect('/recept')
    else:
        return render(request,'recept/bill_final.html')

'''def del_success(request):
    conn = mysql.connector.connect(user = 'root',password = 'root',host = 'localhost',database = 'trial')
    mycursor = conn.cursor()
    usrname = request.session()
    query='delete from table where usrname='
    mycursor.execute(query)
    result=mycursor.fetchall()
    return render(request,'recept/del_success.html')'''

def index_recept(request):
    conn = mysql.connector.connect(user = 'root',password = 'root',host = 'localhost',database = 'trial')
    mycursor = conn.cursor()
    uid = request.session['uid']
    query1 = "select timing from doctor where id = '" + str(uid) +"'"
    mycursor.execute(query1,())
    time = mycursor.fetchone()
    return render(request,'recept/index_recept.html',{'time':time})

def view_appoint(request):
    conn = mysql.connector.connect(user = 'root',password = 'root',host = 'localhost',database = 'trial')
    mycursor = conn.cursor()
    query="select * from appoint"
    mycursor.execute(query)
    result=mycursor.fetchall()
    return render(request,'recept/view_appoint.html',{'result':result})

def show_bill(request):
    conn = mysql.connector.connect(user = 'root',password = 'root',host = 'localhost',database = 'trial')
    mycursor = conn.cursor()
    #uid=request.session["uid"]
    query="select * from bill"
    mycursor.execute(query)
    res=mycursor.fetchall()
    conn.commit()
    conn.close()
    return render(request,'recept/view_bills.html',{'result':res})