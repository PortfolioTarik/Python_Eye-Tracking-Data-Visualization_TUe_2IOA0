# Generated and coded by Tarik Hacialiogullari except when noted.

# Idea & Implementation Tarik & Fanni
# First template by Fanni Egresits
# Updated plot and connected query data set by Tarik Hacialiogullari
from django.shortcuts import render

from django.http import HttpResponse
from bokeh.models import ColumnDataSource, Label, LabelSet, Range1d
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file
from import_csv.models import FixationData
from homepage.models import getUserData
import eye_tracking_visualizations_group23a.settings
from PIL import Image
import requests
from io import BytesIO
from django.contrib.staticfiles.storage import staticfiles_storage


# Add userdata with custom color to the graph and send new graph with userdata in it back.
def addUserToGraph(userData, p, color):
    user = userData['user'].iloc[0]
    sizePath = len(userData.index)
    x_coordinates = userData["MappedFixationPointX"]
    y_coordinates = userData["MappedFixationPointY"]
    texts = list(range(1, sizePath + 1))
    sizes = [userData["FixationDuration"].iloc[[i]] /
             15 for i in list(range(0, sizePath))]
    source = ColumnDataSource(data=dict(x_coordinates=x_coordinates,
                                        y_coordinates=y_coordinates,
                                        texts=texts,
                                        sizes=sizes))
    # ---Start Coding by Fanni Egresits & Tarik Hacialiogullari
    # line
    p.line(x_coordinates, y_coordinates,
           legend_label=user, line_width=2, color=color)
    # nodes
    p.circle('x_coordinates', 'y_coordinates', fill_color="black",
             color=color, size='sizes', line_width=3, source=source)
    # texts
    p.add_layout(LabelSet(x='x_coordinates', y='y_coordinates', text='texts', level='overlay',
                          x_offset=5, y_offset=5, text_color=color, source=source, render_mode='canvas'))
    # ---End Coding by Fanni Egresits & Tarik Hacialiogullari
    return

# ---Start Coding by Fanni Egresits
# generate graph with background and return it.
def getGraph(toolbar, url, w, h, percent = 100):
    #Create plot
    p = figure(plot_width=int((800/100) * percent), plot_height=int((600/100) * percent), x_range=(0, w), y_range=(0, h),
               title="Areas of interest", x_axis_label='Mapped Fixation Point X',
               y_axis_label='Mapped Fixation Point Y', tools=toolbar)

    #Set Background
    p.image_url(url=[url], x=0, y=h, w=w, h=h)
    return p

# ---End Coding by Fanni Egresits


# home is is not in use. just if someone wants to use this for now.
def home(request):
    # toolbar = "box_select, lasso_select, wheel_zoom, pan, reset, save, hover, help"
    # df_userOne = getUserData('p1', '06_Hamburg_S1.jpg', 'color')
    # df_userTwo = getUserData('p16', '06_Hamburg_S1.jpg', 'color')
    # df_userThree = getUserData('p12', '06_Hamburg_S1.jpg', 'color')

    # p = getGraph(toolbar, '06_Hamburg_S1.jpg', request)
    # addUserToGraph(df_userOne, p, 'red')
    # addUserToGraph(df_userTwo, p, 'yellow')
    # addUserToGraph(df_userThree, p, 'blue')
    p = ''

    script, div = components(p)
    return render(request, 'website_starplot.html',
                  {'script': script, 'div': div})
