from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    context = {
        'age': 22,
        'name': 'Fanni'
    }
    return render(request, 'website_starplot.html', context)
