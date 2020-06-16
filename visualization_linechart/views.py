# Coded and generated by Tarik Hacialiogullari, except where noted.
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
    #Select Timestamp and Fixation duration to use it as axes.
    firstUser = False
    if(p.x_range.factors == ['0']):
        firstUser = True
    y = userData['FixationDuration']
    user = userData['user'].iloc[0]
    sizePath = len(userData.index) + len(p.x_range.factors)
    amount_of_fixations = list(range(len(p.x_range.factors), sizePath))
    if firstUser:
        sizePath = len(userData.index)
        amount_of_fixations = list(range(0, sizePath))
    
#---Start Coding by Omar Salem
    #Creating Line and dots
    p.line(amount_of_fixations, y, legend_label=user, line_width=2, color=color)
    p.circle(amount_of_fixations, y, fill_color="black",
              color=color, size=6)
#---End Coding by Omar Salem

    if(firstUser):
        p.x_range.factors = list(userData["Timestamp"].astype(str).to_numpy())
    else:
        p.x_range.factors = list(p.x_range.factors) + \
            list(userData["Timestamp"].astype(str).to_numpy())
    return


#---Start Coding by Omar Salem & Updated by Tarik Hacialiogullari
#Putting Toolbar and creatig Linechart
def getGraph(toolbar, width = 600, height = 450):
    text_x_axis = ['0']
    p = figure(plot_width=width, plot_height=height, y_range=(100, 900),  x_range=text_x_axis,
                title="Line Chart of Fixation Duration per Timestamp", x_axis_label='Timestamp',
                y_axis_label='FixationDuration', tools=toolbar)
    return p
#---Start Coding by Omar Salem & Updated by Tarik Hacialiogullari

def home(request):
    toolbar = "box_select, lasso_select, wheel_zoom, pan, reset, save, hover, help"
    p = getGraph(toolbar)
    #addUserToGraph(getUserData('p1', '06_Hamburg_S1.jpg', 'color', 'red'), p)
    #addUserToGraph(getUserData('p16', '06_Hamburg_S1.jpg', 'color', 'yellow'), p, 'yellow')
    #addUserToGraph(getUserData('p12', '06_Hamburg_S1.jpg', 'color', 'blue'), p, 'blue')

    script, div = components(row(p))
    return render(request, 'website_starplot.html',
                  {'script': script, 'div': div})