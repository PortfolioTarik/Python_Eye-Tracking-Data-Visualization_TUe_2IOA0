from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    context = {
        'var': 10
    }
    return render(request, 'website_scatterplot.html', context)
