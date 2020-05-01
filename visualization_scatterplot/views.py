from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file
import os
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6


def home(request):

    workpath = os.path.dirname(os.path.abspath(__file__))
    df = pd.read_csv(workpath +
                     '/csv/all_fixation_data_cleaned_up.csv', encoding='unicode_escape', sep="\t")
    # df = pd.read_csv('C:/Users/Egresits fanni/Documents/TUe Eindhoven/2IOA0 - HTI Webtech/all_fixation_data_cleaned_up.csv')
    # print(df.head())
    test = df[['user', 'StimuliName']].copy()
    # print(test[(test['StimuliName'] == '07_Moskau_S1.jpg') & (test['user'] == 'p1')])

    # print(test[test['user'] == "p2"] & test[test['StimuliName'] == "07_Moskau_S1.jpg"])
    # prepare some data 3 criteria
    x = df[(test['StimuliName'] == '06_Hamburg_S1.jpg') &
           (test['user'] == 'p1')]["MappedFixationPointX"]

    fruits = ['(x1,y2)', '(x2,y2)', '(x4,y4)',
              '(x5,y5)', '(x6,y6)', '(x7,y8)']
    counts = [5, 3, 4, 2, 4, 6]

    p = figure(x_range=fruits, plot_height=250, title="Fruit Counts",
               toolbar_location=None, tools="")

    p.vbar(x=fruits, top=counts, width=0.9)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    # show the results
    script, div = components(p)
    context = {
        'age': 22,
        'name': 'Omar'
    }
    return render(request, 'website_scatterplot.html',
                  {'script': script, 'div': div})
