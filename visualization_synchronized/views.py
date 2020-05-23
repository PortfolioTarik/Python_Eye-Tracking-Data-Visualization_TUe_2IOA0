# THIS PAGE WILL BE DELETED SO NO COMMENTS.
from django.shortcuts import render
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
from bokeh.layouts import gridplot


def home(request):
    # here include all graphs from import and show them

    # show the results
    script = ''
    tools = "box_select, lasso_select, wheel_zoom, pan, reset, save, hover, help"
    div = '<h1>Line chart</h1><br><h1>Bar chart</h1><br><h1>Heatmap</h1><br><h1>Gaze plot</h1>'

    workpath = os.path.dirname(os.path.abspath(__file__))
    df = pd.read_csv(workpath +
                     '/csv/all_fixation_data_cleaned_up.csv', encoding='unicode_escape', sep="\t")
    # copy dataset with specialized columns (By Fanni)
    test = df[['user', 'StimuliName']].copy()
    userOne = df[(test['StimuliName'] == '06_Hamburg_S1.jpg')
                 & (test['user'] == 'p1')]
    # userTwo = df[(test['StimuliName'] == '06_Hamburg_S1.jpg')
    #              & (test['user'] == 'p16')]
    # create a new plot with a title and axis labels (by Fanni)
    p = figure(plot_width=800, plot_height=600, x_range=(0, 1651), y_range=(0, 1200),
               title="Gaze plot of Hamburg of users", x_axis_label='Mapped Fixation Point X',
               y_axis_label='Mapped Fixation Point Y', tools=tools)
    # background
    p.image_url(url=[
        'https://i.ibb.co/VQSkMnN/06-Hamburg-S1.jpg'], x=0, y=1200, w=1651, h=1200)

    # adding users to the graoh
    color = 'red'

    userData = userOne.copy()
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

    p1 = figure(plot_height=250,
                title="Line chart of Hamburg of users", x_axis_label='Mapped Fixation Point X',
                y_axis_label='Mapped Fixation Point Y', tools=tools)

    # add a line renderer with legend and line thickness
    p1.line(x_coordinates, y_coordinates,
            legend_label="P1.", line_width=2, color="red")
    p1.circle('x_coordinates', 'y_coordinates', fill_color="black",
              color="red", size=6, source=source)
    p1.xgrid.grid_line_color = None
    p1.y_range.start = 0

    p = gridplot([[p1, p]])
    script, div = components(p)
    #script, div = components(row(p1,p2,p3,p4))
    return render(request, 'website_synchronized.html',
                  {'script': script, 'div': div})
