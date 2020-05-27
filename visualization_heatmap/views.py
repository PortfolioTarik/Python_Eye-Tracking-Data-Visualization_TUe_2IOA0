# Generated and coded by Tarik Hacialiogullari except where noted.

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import row
import plotly.graph_objects as go
import plotly.offline as offline
from PIL import Image
from import_csv.models import FixationData
from homepage.models import getUserData



def getGraph(df_user):
    x = df_user["MappedFixationPointX"]
    y = df_user["MappedFixationPointY"]

    layout = go.Layout(
        title='Contourplot area of interest',
        autosize=False,
        width=800,
        height=600,
        images=[dict(
            source='https://i.ibb.co/VQSkMnN/06-Hamburg-S1.jpg',
            xref="x",
            yref="y",
            x=-210,
            y=1250,
            sizex=1950,
            sizey=1500,
            sizing="fill",
            opacity=0.6,
            layer="above")])

    fig = go.Figure( go.Histogram2dContour(
        x =x,
        y = y,
        colorscale = "Hot",
        reversescale = True,
    ), layout)

    #---Start Coding by Andrada Pancu

    fig.update_layout(
        updatemenus=[
            dict(
                buttons=list([ #---End Coding by Andrada
                    dict( #---Start Coding by Fanni Egresits
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
                    #---Start Coding by Andrada
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.5,
                    xanchor="left",
                    y=1.14,
                    yanchor="top"
                ),
            ]
        )

    fig.update_layout(
        annotations=[
            dict(text="Colorscale", x=0, xref="paper", y=1.06,
                yref="paper", showarrow=False),
            dict(text="Stimuli", x=0.4, xref="paper", y=1.06, yref="paper",
                showarrow=False)
            ])#---End Coding by Andrada Pancu

    fig.update_layout(template="plotly_white")
    graph = fig.to_html(
        full_html=False, default_height=500, default_width=1000)

    return graph


def home(request):

    df_user = getUserData('p1', '06_Hamburg_S1.jpg')
    graph = getGraph(df_user)

    script = ""

    return render(request, 'website_boxplot.html',
                  {'script': script, 'div': graph, 'div2': graph})
