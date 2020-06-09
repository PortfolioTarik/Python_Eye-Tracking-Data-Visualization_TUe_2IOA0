# Generated and coded by Omar Salem except when noted.

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
#--- Select Timestamp and Fixation duration on graph 
    x = userData['Timestamp']
    y = userData['FixationDuration']
#---Start Coding by Tarik Haci
    user = userData['user'].iloc[0]
    #---End Coding by Tarik Haci
    #Creating Line and dots
    p.line(x, y, legend_label=user, line_width=2, color=color)
    p.circle(x, y, fill_color="black",
              color=color, size=6)

    return

#---Putting Toolbar and creatig Linechart
def getGraph(toolbar):
    p = figure(plot_width=600, plot_height=450, y_range=(100, 700),
                title="Line Chart of Fixation Duration per Timestamp", x_axis_label='Timestamp',
                y_axis_label='FixationDuration', tools=toolbar)
    return p

#---Start Coding by Tarik Haci
def home(request):
    toolbar = "box_select, lasso_select, wheel_zoom, pan, reset, save, hover, help"
    p = getGraph(toolbar)
    addUserToGraph(getUserData('p1', '06_Hamburg_S1.jpg', 'color', 'red'), p)
    addUserToGraph(getUserData('p16', '06_Hamburg_S1.jpg', 'color', 'yellow'), p, 'yellow')
    addUserToGraph(getUserData('p12', '06_Hamburg_S1.jpg', 'color', 'blue'), p, 'blue')

    script, div = components(row(p))
    return render(request, 'website_starplot.html',
                  {'script': script, 'div': div})
#--- End Coding by Tarik Haci
