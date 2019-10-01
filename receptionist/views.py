from django.shortcuts import render

# Create your views here.

def receptionist(request):
    return render(request,'receptionist.html')    