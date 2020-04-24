from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1> This webpage will be dedicated to visualization of Linecharts</h1>')
