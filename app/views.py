from django.shortcuts import render
from django.http import HttpResponse

def abc(request):
    return HttpResponse('MESSAGE')

def pqr(request):
    return HttpResponse('<h1>Message Displayed</h1>')