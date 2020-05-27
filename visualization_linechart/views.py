# Generated and coded by Tarik Hacialiogullari except when noted.

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import row
from homepage.models import getUserData


def addUserToGraph(userData, p, color):
    x = userData['Timestamp']
    y = userData['FixationDuration']
    user = userData['user'].iloc[0]
    #---Start Coding by Omar Salim & Updated by Tarik Hacialiogullari
    p.line(x, y, legend_label=user, line_width=2, color=color)
    p.circle(x, y, fill_color="black",
              color=color, size=6)
    #---End Coding by Omar Salim & Updated by Tarik Hacialiogullari

    return

def getGraph(toolbar):
    #---Start Coding by Omar Salim & Updated by Tarik Hacialiogullari
    p = figure(plot_width=600, plot_height=450, x_range=(38000, 43000), y_range=(100, 700),
                title="Fixation Duration per point for color", x_axis_label='Timestamp',
                y_axis_label='FixationDuration', tools=toolbar)
    #---End Coding by Omar Salim & Updated by Tarik Hacialiogullari
    return p

def home(request):
    toolbar = "box_select, lasso_select, wheel_zoom, pan, reset, save, hover, help"
    p = getGraph(toolbar)
    addUserToGraph(getUserData('p1', '06_Hamburg_S1.jpg', 'color'), p, 'red')
    addUserToGraph(getUserData('p16', '06_Hamburg_S1.jpg', 'color'), p, 'yellow')
    addUserToGraph(getUserData('p12', '06_Hamburg_S1.jpg', 'color'), p, 'blue')

    script, div = components(row(p))
    return render(request, 'website_starplot.html',
                  {'script': script, 'div': div})
