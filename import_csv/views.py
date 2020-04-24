from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    context = {
        'var': functiontwo(10)
    }
    return render(request, 'website_import.html', context)


def functiontwo(input):
    return input + 5
