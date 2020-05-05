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


def home(request):

    workpath = os.path.dirname(os.path.abspath(__file__))
    path = '/csv/all_fixation_data_cleaned_up.csv'
    df = pd.read_csv(workpath +
                     '/all_fixation_data_cleaned_up.csv', encoding='unicode_escape', sep="\t")

    # copy dataset with specialized columns (just for testing something)
    test = df[['user', 'StimuliName']].copy()
    # prepare some data 3 criteria
    x = df[(test['StimuliName'] == '06_Hamburg_S1.jpg') &
           (test['user'] == 'p1')]["MappedFixationPointX"]
    y = df[(test['StimuliName'] == '06_Hamburg_S1.jpg') &
           (test['user'] == 'p1')]["MappedFixationPointY"]

    z = df[(test['StimuliName'] == '06b_Hamburg_S2.jpg') &
           (test['user'] == 'p16')]["MappedFixationPointX"]
    w = df[(test['StimuliName'] == '06b_Hamburg_S2.jpg') &
           (test['user'] == 'p16')]["MappedFixationPointY"]

    img = Image.open(workpath + '/06_Hamburg_S1.jpg')

    layout = go.Layout(
        title='My title',
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
        colorscale='Blues'
    ), layout)

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

    fig2 = go.Figure(go.Histogram2dContour(
        x=z,
        y=w,
        colorscale='Blues'
    ), layout)

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
    graph2 = fig2.to_html(
        full_html=False, default_height=500, default_width=1000)
    script = ""

    return render(request, 'website_boxplot.html',
                  {'script': script, 'div': graph, 'div2': graph2})
