# Coded by Tarik Hacialiogullari unless when stated
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from bokeh.models import ColumnDataSource, Label, LabelSet, Range1d
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file
import os
from import_csv.models import FixationData


def addUserToGraph(userDataOriginal, p, color):
    userData = userDataOriginal.copy()
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


def home(request):
    all_data = FixationData.objects.all()
    type(all_data)
    print(all_data)
    df_test = pd.DataFrame(list(all_data))
    print(df_test.info)
    # df_test.head()

    workpath = os.path.dirname(os.path.abspath(__file__))
    df = pd.read_csv(workpath +
                     '/all_fixation_data_cleaned_up.csv', encoding='unicode_escape', sep="\t")
    # copy dataset with specialized columns (By Fanni)
    test = df[['user', 'StimuliName']].copy()
    userData = df[(test['StimuliName'] == '06_Hamburg_S1.jpg')
                  & (test['user'] == 'p1')]
    userData2 = df[(test['StimuliName'] == '06_Hamburg_S1.jpg')
                   & (test['user'] == 'p16')]
    # create a new plot with a title and axis labels (by Fanni)
    p = figure(plot_width=800, plot_height=600, x_range=(0, 1651), y_range=(0, 1200),
               title="Gaze plot of Hamburg of users", x_axis_label='Mapped Fixation Point X',
               y_axis_label='Mapped Fixation Point Y', tools="box_select, wheel_zoom, pan, reset, save, hover")
    # background
    p.image_url(url=[
        'https://i.ibb.co/VQSkMnN/06-Hamburg-S1.jpg'], x=0, y=1200, w=1651, h=1200)

    # adding users to the graoh
    addUserToGraph(userData, p, 'red')
    addUserToGraph(userData2, p, 'yellow')
    # show the results
    script, div = components(p)
    return render(request, 'website_starplot.html',
                  {'script': script, 'div': div})
