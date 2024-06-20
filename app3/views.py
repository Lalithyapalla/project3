from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def fun3(request):
    return HttpResponse('Message3')
def fun4(request):
    return HttpResponse('Message4')