# By Tarik Hacialiogullari & Fanni
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import row
import os
import plotly.graph_objects as go
import plotly.offline as offline
from PIL import Image
from import_csv.models import FixationData


def getUserData(user, mapName):
    columns = ['ID', 'Timestamp', 'StimuliName', 'FixationIndex', 'FixationDuration',
               'MappedFixationPointX', 'MappedFixationPointY', 'user', 'description']
    columns_sql = ', '.join(columns)
    queryset_userData = FixationData.objects.raw(
        "SELECT " + columns_sql + " FROM Fixation_data WHERE user = '" + user + "' AND StimuliName LIKE '%" + mapName + "' ")
    return querySetToPandas(queryset_userData)


def querySetToPandas(queryset_userData):
    dtypes = np.dtype([
        ('Timestamp', int),
        ('StimuliName', str),
        ('FixationIndex', int),
        ('FixationDuration', int),
        ('MappedFixationPointX', int),
        ('MappedFixationPointY', int),
        ('user', str),
        ('description', str)
        ])
    data = np.empty(0, dtype=dtypes)
    userData = pd.DataFrame(data)

    for fixatData in queryset_userData: 
        dics = dict(
                        Timestamp = fixatData.Timestamp, 
                        StimuliName = str(fixatData.StimuliName), 
                        FixationIndex = fixatData.FixationIndex, 
                        FixationDuration = fixatData.FixationDuration, 
                        MappedFixationPointX = fixatData.MappedFixationPointX, 
                        MappedFixationPointY = fixatData.MappedFixationPointY, 
                        user = str(fixatData.user), 
                        description = str(fixatData.description)
                    )
        userData = userData.append(dics, ignore_index=True)
    return userData



def home(request):

    df_user = getUserData('p1', '06_Hamburg_S1.jpg')
    x = df_user[(df_user['StimuliName'] == '06_Hamburg_S1.jpg') &
           (df_user['user'] == 'p1')]["MappedFixationPointX"]
    y = df_user[(df_user['StimuliName'] == '06_Hamburg_S1.jpg') &
           (df_user['user'] == 'p1')]["MappedFixationPointY"]
    # img = Image.open(workpath + '/06_Hamburg_S1.jpg')

    layout = go.Layout(
        title='Contourplot area of interest',
        autosize=False,
        width=750,
        height=500,
        images=[dict(
            source='https://i.ibb.co/VQSkMnN/06-Hamburg-S1.jpg',
            xref="x",
            yref="y",
            x=0,
            y=1200,
            sizex=1651,
            sizey=1200,
            sizing="stretch",
            opacity=0.7,
            layer="above")])

    fig = go.Figure(go.Histogram2dContour(
        x=x,
        y=y,
        colorscale='Hot',
        reversescale=True,

 ), layout)


    fig.update_layout(
        updatemenus=[
            dict(
                buttons=list([
                    dict(
                        args=["type", "heatmap"],
                        label="Antwerpen",
                        method="update"
                    ),
                    dict(
                        args=["type", "heatmap"],
                        label="Berlin",
                        method="update"
                    ),
                    dict(
                        args=["type", "heatmap"],
                        label="Bordeaux",
                        method="update"
                    ),
                    dict(
                        args=["type", "heatmap"],
                        label="Köln",
                        method="update"
                    ),
                    dict(
                        args=["type", "heatmap"],
                        label="Frankfurt",
                        method="update"
                    ),
                    dict(
                        args=["type", "heatmap"],
                        label="Hamburg",
                        method="update"
                    ),
                    dict(
                        args=["type", "heatmap"],
                        label="Moskau",
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
            #Dropdown colorscale by Fanni Egresits
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


                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.12,
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
        ])
# # Add annotation
#     fig.update_layout(
#         annotations=[
#             dict(text="Stimuli:", showarrow=False,
#             x=0, y=1.085, yref="paper", align="left"),
#             dict(text="Color:", showarrow=False,
#                  x=0, y=1.085, yref="paper", align="right")
#         ]
#     )

    # fig.update_layout(
    #     autosize=False,
    #     width=700,
    #     height=600,
    #     #  margin=dict(
    #     #      l=50,
    #     #      r=50,
    #     #      b=100,
    #     #      t=100,
    #     #      pad=4
    #     #  )
    # )
    # fig.add_layout_image(
    #     dict(
    #         # source=img,
    #         source='https://i.ibb.co/VQSkMnN/06-Hamburg-S1.jpg',
    #         xref="x",
    #         yref="y",
    #         x=0,
    #         y=1200,
    #         sizex=1651,
    #         sizey=1200,
    #         sizing="contain",
    #         opacity=0.5,
    #         visible=True,
    #         layer="above")
    # )

    # fig2 = go.Figure(go.Histogram2dContour(
    #     x=z,
    #     y=w,
    #     colorscale='Blues'
    # ), layout)

    # fig2.update_layout(
    #     autosize=False,
    #     width=700,
    #     height=600,
    #     #  margin=dict(
    #     #      l=50,
    #     #      r=50,
    #     #      b=100,
    #     #      t=100,
    #     #      pad=4
    #     #  )
    # )
    # fig2.add_layout_image(
    #     dict(
    #         # source=img,
    #         source='https://images.plot.ly/language-icons/api-home/python-logo.png',
    #         xref="x",
    #         yref="y",
    #         x=0,
    #         y=0,
    #         sizex=500,
    #         sizey=300,
    #         sizing="contain",
    #         opacity=0.7,
    #         visible=True,
    #         layer="below")
    # )
    # # fig.show()
    # fig.write_html("file2.html")
    # show the results
    # fig.show()
    fig.update_layout(template="plotly_white")
    graph = fig.to_html(
        full_html=False, default_height=500, default_width=1000)

    script = ""

    return render(request, 'website_boxplot.html',
                  {'script': script, 'div': graph, 'div2': graph})
