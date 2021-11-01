from django.http import HttpResponse
from django.shortcuts import render

def employee(request) :
    return HttpResponse("hello this Abdur Razzak this is my employee page")
def profile(request) :
    return render(request,'employee/profile.html')