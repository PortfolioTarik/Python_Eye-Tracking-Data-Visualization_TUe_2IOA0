#Coded by Youssef Selim

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Label, LabelSet, Range1d
from bokeh.layouts import row
from bokeh.embed import components
import numpy as np
import pandas as pd
import os
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.io import output_file, show


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
           (test['user'] == 'p1')]["Timestamp"]**(1/2)
    y= df[(test['StimuliName'] == '06_Hamburg_S1.jpg') &
           (test['user'])]["FixationDuration"]
    z = df[(test['StimuliName'] == '06b_Hamburg_S2.jpg') &
           (test['user'] == 'p16')]["Timestamp"]**(1/2)
    w = df[(test['StimuliName'] == '06b_Hamburg_S2.jpg') &
           (test['user'] == 'p16')]["FixationDuration"]
    f = df[(test['StimuliName'] == '06_Hamburg_S1.jpg') &
           (test['user'])]["Timestamp"]**(1/2)

    s1 = figure(
     plot_height=250, title="Bar chart of hamburg for user 1(color)", x_axis_label='Timestamp', y_axis_label='Fixation Duration',
               toolbar_location="right", tools="box_select, wheel_zoom, pan, reset, save, hover")
    
    s2 = figure(
     plot_height=250, title="Bar chart of hamburg for user 16(gray)",x_axis_label='Timestamp', y_axis_label='Fixation Duration',
               toolbar_location="right", tools="box_select, wheel_zoom, pan, reset, save, hover")

    s1.vbar(x=f, top=y, width=0.05, color = 'red', legend_label="p1")
    s2.vbar(x=z, top=w, width =0.05, color ='green', legend_label="P16")
    
    s1.xgrid.grid_line_color = None
    s1.y_range.start = 0
    s2.xgrid.grid_line_color = None
    s2.y_range.start = 0
    p = s1


    # show the results
    script, div = components(p)
    context = {
        'age': 18,
        'name': 'Youssef'
    }
    return render(request, 'website_scatterplot.html',
                  {'script': script, 'div': div})
