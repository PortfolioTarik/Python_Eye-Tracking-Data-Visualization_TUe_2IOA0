# Generated and coded by Tarik Hacialiogullari except when noted.
# Idea & Implementation Tarik & Fanni
# First template by Fanni Egresits
# Updated plot and connected query data set by Tarik Hacialiogullari
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from bokeh.models import ColumnDataSource, Label, LabelSet, Range1d
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file
from import_csv.models import FixationData
from homepage.models import getUserData


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
    # line
    p.line(x_coordinates, y_coordinates,
           legend_label=user, line_width=2, color=color)
    # nodes
    p.circle('x_coordinates', 'y_coordinates', fill_color="black",
             color=color, size='sizes', line_width=3, source=source)
    # texts
    p.add_layout(LabelSet(x='x_coordinates', y='y_coordinates', text='texts', level='overlay',
                          x_offset=5, y_offset=5, text_color=color, source=source, render_mode='canvas'))
    return


def getGraph(toolbar):
    p = figure(plot_width=800, plot_height=600, x_range=(0, 1651), y_range=(0, 1200),
               title="Gaze plot of Hamburg of users", x_axis_label='Mapped Fixation Point X',
               y_axis_label='Mapped Fixation Point Y', tools=toolbar)
    # background
    p.image_url(url=[
        'https://i.ibb.co/VQSkMnN/06-Hamburg-S1.jpg'], x=0, y=1200, w=1651, h=1200)

    # counter = 0
    # color = 'red'
    # for userData in usersData:
    #     if(counter == 1):
    #         color = 'yellow'
    #     if(counter == 2):
    #         color = 'blue'
    #     addUserToGraph(userData, p, color)
    #     counter = counter + 1

    return p


def home(request):
    df_userOne = getUserData('p1', '06_Hamburg_S1.jpg')
    df_userTwo = getUserData('p16', '06_Hamburg_S1.jpg')
    df_userThree = getUserData('p12', '06_Hamburg_S1.jpg')

    p = getGraph()
    addUserToGraph(df_userOne, p, 'red')
    addUserToGraph(df_userTwo, p, 'yellow')
    addUserToGraph(df_userThree, p, 'blue')


    script, div = components(p)
    return render(request, 'website_starplot.html',
                  {'script': script, 'div': div})
