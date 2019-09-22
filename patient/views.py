from django.shortcuts import render

# Create your views here.

def patient(request):
    return render(request,'patient.html')    

def appointment(request):
    return render(request,'patient/appointment.html')