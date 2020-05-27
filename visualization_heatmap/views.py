# Generated and coded by Tarik Hacialiogullari except when noted.

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



def getGraph(cnt):
    cnt = 1
    #x = df_user["MappedFixationPointX"]
    #y = df_user["MappedFixationPointY"]

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

    fig = go.Figure( layout = layout )

    #---Start Coding by Andrada
    query_maps = FixationData.objects.raw(
        "SELECT DISTINCT StimuliName, 1 as id FROM Fixation_data ")

    query_users = FixationData.objects.raw(
        "SELECT DISTINCT user, 1 as id FROM Fixation_data ")

    stimuli_list = ["StimuliName:"]
    user_list = ['User:']

    for stimulidata in query_maps: 
        stimuli_list.append(stimulidata.StimuliName)
    
    for userdata in query_users: 
        user_list.append(userdata.user)

    for i in range(1,len(user_list)):
        #if stimuli_list[i] != "StimuliName:":
        bool_visible = False
        if i == 1:
            bool_visible = True
        fig.add_trace(
            go.Histogram2dContour( x = getUserData(user_list[i], stimuli_list[i])["MappedFixationPointX"] ,
                y = getUserData(user_list[i], stimuli_list[i])["MappedFixationPointY"],
                name = stimuli_list[i], visible = bool_visible ))

    fig.update_layout(
        updatemenus=[
            dict(
                buttons=list([
                    dict(
                        args=[{"visible": [True, False, False, False, False, False, False]},
                        {"title": stimuli_list[1],
                        "annotations": []}],
                        label=stimuli_list[1],
                        method="update"
                    ),
                    dict(
                            args=[{"visible": [False, True, False, False, False, False, False]},
                            {"title": stimuli_list[2],
                            "annotations": []}],
                            label=stimuli_list[2],
                            method="update"
                    ),
                    dict(
                            args=[{"visible": [False, False, True, False, False, False, False]},
                            {"title": stimuli_list[3],
                            "annotations": []}],
                            label=stimuli_list[3],
                            method="update"
                    ),
                    dict(
                            args=[{"visible": [False, False, False, True, False, False, False]},
                            {"title": stimuli_list[4],
                            "annotations": []}],
                            label=stimuli_list[4],
                            method="update"
                    ),
                    dict(
                            args=[{"visible": [False, False, False, False, True, False, False]},
                            {"title": stimuli_list[5],
                            "annotations": []}],
                            label=stimuli_list[5],
                            method="update"
                    ),
                    dict(
                            args=[{"visible": [False, False, False, False, False, True, False]},
                            {"title": stimuli_list[6],
                            "annotations": []}],
                            label=stimuli_list[6],
                            method="update"
                    ),
                    dict(
                            args=[{"visible": [False, False, False, False, False, False, True]},
                            {"title": stimuli_list[7],
                            "annotations": []}],
                            label=stimuli_list[7],
                            method="update"
                        ),
                ]),
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.5,
                    xanchor="left",
                    y=1.14,
                    yanchor="top"
            ),
                #---End Coding by Andrada
                #---Start Coding by Fanni Egresits
                dict(
                    buttons=list([
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
                    #---Start Coding by Andrada
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.12,
                    xanchor="left",
                    y=1.14,
                    yanchor="top"
                ),
            ]
        )#---End Coding by Andrada Pancu

    fig.update_layout(
        annotations=[
            dict(text="Colorscale", x=0, xref="paper", y=1.06,
                yref="paper", showarrow=False),
            dict(text="Stimuli", x=0.4, xref="paper", y=1.06, yref="paper",
                showarrow=False)
            ])

    fig.update_layout(template="plotly_white")
    #---End Coding by Fanni Egresits
    graph = fig.to_html(
        full_html=False, default_height=500, default_width=1000)

    return graph


def home(request):

    #df_user = getUserData('p1', '06_Hamburg_S1.jpg')
    graph = getGraph(cnt)

    script = ""

    return render(request, 'website_boxplot.html',
                  {'script': script, 'div': graph, 'div2': graph})
