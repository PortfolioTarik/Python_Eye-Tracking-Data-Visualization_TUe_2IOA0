# Generated and coded by Tarik Hacialiogullari except when noted.

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Label, LabelSet, Range1d
from bokeh.layouts import row
from bokeh.embed import components
import numpy as np
import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.io import output_file, show
from homepage.models import getUserData


def addUserToGraph(userDataOriginal, p, color, start_index):
    userData = userDataOriginal.copy()
    user = userData['user'].iloc[0]
    sizePath = len(userData.index) + start_index
    # x_coordinates = userData["Timestamp"]**(1/2)
    y_coordinates = userData["FixationDuration"]
    amount_of_fixations = list(range(start_index, sizePath))
    # source = ColumnDataSource(data=dict(x_coordinates=x_coordinates,
    #                                    y_coordinates=y_coordinates))

    #---Start Coding by Youssef Selim
    p.vbar(x=amount_of_fixations, top=y_coordinates,
           width=0.05, color=color, legend_label=user)
    #---End Coding by Youssef Selim

    if(start_index == 0):
        p.x_range.factors = list(userData["Timestamp"].astype(str).to_numpy())
    else:
        p.x_range.factors = list(p.x_range.factors) + \
            list(["gap" + str(start_index + x) for x in range(10)]) + \
            list(userData["Timestamp"].astype(str).to_numpy())

    return

def getGraph(toolbar, end):
    start = 1000
    
    text_x_axis = list(range(start, end))
    text_x_axis = [str(x) for x in text_x_axis]

    #---Start Coding by Youssef Selim
    p = figure(
        plot_height=300, plot_width=800, title="Bar chart of hamburg for user 1(color)", x_axis_label='Timestamp', y_axis_label='Fixation Duration',
        toolbar_location="right", tools=toolbar,  x_range=text_x_axis)
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    #---End Coding by Youssef Selim

    return p

def home(request):
    toolbar = "box_select, lasso_select, wheel_zoom, pan, reset, save, hover, help"
    df_userOne = getUserData('p1', '06_Hamburg_S1.jpg')
    df_userTwo = getUserData('p16', '06_Hamburg_S1.jpg')
    df_userThree = getUserData('p12', '06_Hamburg_S1.jpg')

    end = len(df_userOne.index) + 10 + len(df_userTwo.index) + 10 + 1000
    p = getGraph(toolbar, end)
    addUserToGraph(df_userOne, p, 'red', 0)
    addUserToGraph(df_userTwo, p, 'yellow', len(df_userOne.index) + 10)
    addUserToGraph(df_userThree, p, 'blue', len(df_userOne.index) + 10 + len(df_userTwo.index) + 10)

    # show the results
    script, div = components(p)
    return render(request, 'website_scatterplot.html',
                  {'script': script, 'div': div})
