and

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
    p.line(x, y, legend_label=user, line_width=2, color=color)
    p.circle(x, y, fill_color="black",
              color=color, size=6)

    return

def getGraph(toolbar):
    p = figure(plot_width=600, plot_height=400, x_range=(38000, 43000), y_range=(100, 700),
                title="Fixation Duration per point for color", x_axis_label='Timestamp',
                y_axis_label='FixationDuration', tools=toolbar)

    return p

def home(request):
    p = getGraph()
    addUserToGraph(getUserData('p1', '06_Hamburg_S1.jpg'), p, 'red')
    addUserToGraph(getUserData('p16', '06_Hamburg_S1.jpg'), p, 'yellow')
    addUserToGraph(getUserData('p12', '06_Hamburg_S1.jpg'), p, 'blue')

    script, div = components(row(p))
    return render(request, 'website_starplot.html',
                  {'script': script, 'div': div})
