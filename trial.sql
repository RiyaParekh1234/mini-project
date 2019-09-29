show databases;
create database trial;
use trial;
show tables;
create table patient(id int,ht int,wt int,med_history varchar(50));
create table doctor(id int,lic_no int,reg_no int,experience int,degree varchar(30),spltion varchar(30),timing varchar(30),fee int);
create table person(id int,prof varchar(11),usrname varchar(25),addr varchar(30),emailid varchar(30),id_p int,gender varchar(2),dob date,phno int,pswd1 varchar(25),pswd2 varchar(25));
create table receptionist(id int,wrk_hrs int,salary float);
