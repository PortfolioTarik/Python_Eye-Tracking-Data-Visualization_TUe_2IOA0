# Generated and coded by Tarik Hacialiogullari except when noted.

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.models import ColumnDataSource, Label, LabelSet, Range1d
from bokeh.layouts import row, widgetbox
from bokeh.embed import components
import numpy as np
import pandas as pd
from bokeh.models import ColumnDataSource, Select
from bokeh.models.widgets import Dropdown
from bokeh.palettes import Spectral6
from bokeh.io import output_file, show
from homepage.models import getUserData


def addUserToGraph(userData, p, color, start_index, invert):
    if (invert):
        userData = userData.reindex(index=userData.index[::-1])
    user = userData['user'].iloc[0]
    sizePath = len(userData.index) + start_index
    y_coordinates = userData["FixationDuration"]
    amount_of_fixations = list(range(start_index, sizePath))
    #---Start Coding by Youssef Selim
    p.vbar(x=amount_of_fixations, top=y_coordinates,
           width=0.25, color=color, legend_label=user)
    #---End Coding by Youssef Selim

    if(start_index == 0):
        p.x_range.factors = list(userData["Timestamp"].astype(str).to_numpy())
    else:
        p.x_range.factors = list(p.x_range.factors) + \
            list(userData["Timestamp"].astype(str).to_numpy())

    return

def getGraph(toolbar, end, width = 1500, height = 300):
    start = 1000
    
    text_x_axis = list(range(start, end))
    text_x_axis = [str(x) for x in text_x_axis]

    #---Start Coding by Youssef Selim
    #graph visualisation information such as width, titles etc.
    p = figure(
        plot_height=height, plot_width=width, title="Bar chart of hamburg for users", x_axis_label='Timestamp', y_axis_label='Fixation Duration',
        toolbar_location="right", tools=toolbar,  x_range=text_x_axis)
    p.xgrid.grid_line_color = None
    #changes x axis label size and orientation so that the numbers are visible
    p.xaxis.major_label_orientation = 1
    p.xaxis.major_label_text_font_size = "6pt"
    p.y_range.start = 0
    #---End Coding by Youssef Selim

    return p

#By Tarik Hacialiogullari but it is only used to see individual graphs and experiment. (so for coding purposes not for the researchers)
def home(request):
    #toolbar = "box_select, lasso_select, wheel_zoom, pan, reset, save, hover, help"

    # #df_userOne = getUserData('p1', '06_Hamburg_S1.jpg', 'color')
    # #df_userTwo = getUserData('p16', '06_Hamburg_S1.jpg', 'color')
    # #df_userThree = getUserData('p12', '06_Hamburg_S1.jpg', 'color')

    # end = len(df_userOne.index) + len(df_userTwo.index) + 1000
    # p = getGraph(toolbar, end)
    # addUserToGraph(df_userOne, p, 'red', 0)
    # addUserToGraph(df_userTwo, p, 'yellow', len(df_userOne.index))
    # addUserToGraph(df_userThree, p, 'blue', len(df_userOne.index) + len(df_userTwo.index))
    p = ''

    # show the results
    script, div = components(p)
    return render(request, 'website_scatterplot.html',
                  {'script': script, 'div': div})
