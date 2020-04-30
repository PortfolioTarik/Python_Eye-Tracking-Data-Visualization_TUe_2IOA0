from django.shortcuts import render
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import math
import os
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, Legend, LegendItem, Scatter
from bokeh.plotting import figure, output_file, show, output_notebook
from bokeh.models.tools import HoverTool
from bokeh.core.properties import value
from bokeh.palettes import Spectral10, Category20, Category20_17, inferno, magma, viridis
from bokeh.transform import jitter

def home(request):
    #Fixation duration for y axis and Mapped fixation point x or time stamp on
    #x axis and the user to compare each of users with dropdown menu
    dtype = {'Timestamp':np.uint16, 'FixationDuration':np.unit16, 
    'MappedFixationPointX':np.unit16, 'User':str}

    workpath = os.path.dirname(os.path.abspath(__file__))
    path = '/csv/all_fixation_data_cleaned_up.csv'
    df_eye = pd.read_csv(workpath + path, usecols=dtype.keys(), dtype=dtype)
    
    #tools to add to graph
    TOOLS = "pan, wheel_zoom, box_zoom, box_select,reset, save"

    #Build Line chart 
    p = figure(title="Fixation duration and mapped fix", tools = TOOLS)
    p.line(x='MappedFixationPointX', y='FixationDuration')
    p.xaxis.axis_label = 'MappedFixationPointX'
    p.yaxis.axis_label = 'FixationDuration'
    p.xgrid.grid_line_color = None
    show(p)


    
    # Feed them to the Django template.
    return render(request, 'website_linechart.html')
