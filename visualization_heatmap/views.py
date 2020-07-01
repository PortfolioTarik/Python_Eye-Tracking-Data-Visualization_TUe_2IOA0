# Generated and coded by Tarik Hacialiogullari except when noted.

from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import row
import plotly.graph_objects as go
import plotly.offline as offline
from PIL import Image
from io import BytesIO
import requests
from import_csv.models import FixationData
from homepage.models import getUserData
import eye_tracking_visualizations_group23a.settings
import base64
import os


#Added third dimension and colorbar label by Fanni Egresits
def getGraph(df_user, url, w, h, percent = 100):
    x = df_user["MappedFixationPointX"]
    y = df_user["MappedFixationPointY"]
    z = df_user["FixationDuration"]
    #stimuli = df_user["StimuliName"][0]

    layout = go.Layout(
        title='Areas of interest of the user ' + df_user['user'].iloc[0],
        xaxis_title='Mapped Fixation Point X',
        yaxis_title='Mapped Fixation Point Y',
        autosize=False,
        width=int((800/100) * percent),
        height=int((600/100) * percent),
        xaxis = dict(
            range= (0, w),  # sets the range of xaxis
            constrain="domain",  # meanwhile compresses the xaxis by decreasing its "domain"
        ),
        yaxis = dict(
            range= (0, h),  # sets the range of xaxis
            constrain="domain",  # meanwhile compresses the xaxis by decreasing its "domain"
        ),
        images=[dict(
            source=url,
            xref="x",
            yref="y",
            x=0,
            y=h,
            sizex=w,
            sizey=h,
            sizing="stretch",
            opacity=0.7,
            layer="above")])


    fig = go.Figure(go.Histogram2dContour(
        x=x,
        y=y,
        colorscale='Hot',
        reversescale=True,
        colorbar=dict(
            title='Fixation Duration in seconds',  # title here
            titleside='right',
            titlefont=dict(
                size=14,
                family='Arial, sans-serif')
        ),

    ), layout)
   
            #---Start Coding by Andrada
    fig.update_layout(
        updatemenus=[
            dict(
                buttons=list([
            #---End Coding by Andrada
            #---Start Coding by Fanni Egresits
                    dict(
                        args=["colorscale", "Hot"],
                        label="Orange",
                        method="restyle"
                    ),
                    dict(
                        args=["colorscale", "Greys"],
                        label="Grey",
                        method="restyle"
                    ),
                    dict(
                        args=["colorscale", "Greens"],
                        label="Green",
                        method="restyle"
                    ),
                ]),
                #---End Coding by Fanni Egresits
                #---Start Coding by Andrada Pancu
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.12,
                xanchor="left",
                y=1.12,
                yanchor="top"
            ),
        ]
    )

    fig.update_layout(
        annotations=[    
            #---End Coding by Andrada
            #---Start Coding by Fanni Egresits
            dict(text="Colorscale", x=0, xref="paper", y=1.08,
                 yref="paper", showarrow=False),
        ])

    fig.update_layout(template="plotly_white")
           #---End Coding by Fanni Egresits
    graph = fig.to_html(
        full_html=False, default_height=500, default_width=1000)

    return graph


#By Tarik Hacialiogullari but it is only used to see individual graphs and experiment. (so for coding purposes not for the researchers)
def home(request):

    #df_user = getUserData('p1', '06_Hamburg_S1.jpg', 'color')
    #graph = getGraph(df_user, '06_Hamburg_S1.jpg', request)
    graph = ''

    script = ""

    return render(request, 'website_boxplot.html',
                  {'script': script, 'div': graph, 'div2': graph})
