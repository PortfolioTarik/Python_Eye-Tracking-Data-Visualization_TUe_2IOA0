# Generated en coded by Tarik Hacialiogullari
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


webpages = [
    {
        'title': 'Import_csv',
        'url': '/import'
    },
    {
        'title': 'Visualization Heatmap (contour map)',
        'url': '/boxplot'
    },
    {
        'title': 'Visualization Linechart',
        'url': '/linechart'
    },
    {
        'title': 'Visualization Barchart',
        'url': '/scatterplot'
    },
    {
        'title': 'Visualization Gazeplot',
        'url': '/starplot'
    }
]


def home(request):
    context = {
        'webpages': webpages
    }
    return render(request, 'home.html', context)

# def home(request):
#     return HttpResponse('<h1>[2IOA0 Group 23A] <br> Welcome to our eye-tracking-software :)! </h1> <h3>Navigation <br> (yeah it is ugly but better than nothing, atleast it works :D)</h3> <br> <a href="/import">import_csv</a> <br> <a href="/boxplot">vizualization_boxplot</a> <br> <a href="/linechart">vizualization_linechart</a> <br> <a href="/scatterplot">vizualization_scatterplot</a> <br> <a href="/starplot">vizualization_starplot</a>')
