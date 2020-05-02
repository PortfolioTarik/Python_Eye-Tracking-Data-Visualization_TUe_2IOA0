# By Tarik Hacialiogullari & Fanni
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file
import os
import plotly.graph_objects as go
import plotly.offline as offline
from PIL import Image


def home(request):

    workpath = os.path.dirname(os.path.abspath(__file__))
    path = '/csv/all_fixation_data_cleaned_up.csv'
    df = pd.read_csv(workpath +
                     '/all_fixation_data_cleaned_up.csv', encoding='unicode_escape', sep="\t")
    # df = pd.read_csv('C:/Users/Egresits fanni/Documents/TUe Eindhoven/2IOA0 - HTI Webtech/all_fixation_data_cleaned_up.csv')
    # print(df.head())

    # copy dataset with specialized columns (just for testing something)
    test = df[['user', 'StimuliName']].copy()
    # print(test[(test['StimuliName'] == '07_Moskau_S1.jpg') & (test['user'] == 'p1')])

    # print(test[test['user'] == "p2"] & test[test['StimuliName'] == "07_Moskau_S1.jpg"])
    # prepare some data 3 criteria
    x = df[(test['StimuliName'] == '06_Hamburg_S1.jpg') &
           (test['user'] == 'p1')]["MappedFixationPointX"]
    y = df[(test['StimuliName'] == '06_Hamburg_S1.jpg') &
           (test['user'] == 'p1')]["MappedFixationPointY"]

    z = df[(test['StimuliName'] == '06b_Hamburg_S2.jpg') &
           (test['user'] == 'p16')]["MappedFixationPointX"]
    w = df[(test['StimuliName'] == '06b_Hamburg_S2.jpg') &
           (test['user'] == 'p16')]["MappedFixationPointY"]
    # print(z)

    # output to static HTML file
    # output_file("lines.html")

    # # create a new plot with a title and axis labels
    # p = figure(plot_width=800, plot_height=600, x_range=(0, 1651), y_range=(0, 1200),
    #            title="Gaze plot of Hamburg of the first user", x_axis_label='Mapped Fixation Point X',
    #            y_axis_label='Mapped Fixation Point Y')

    # # add a line renderer with legend and line thickness
    # p.line(x, y, legend_label="P1.", line_width=2, color="red")
    # p.line(z, w, legend_label="P16.", line_width=2, color="blue")
    # p.circle(x, y, fill_color="red",
    #          color="red", size=8)

    # # add background
    # p.image_url(url=['../06_Hamburg_S1.jpg'], x=0,
    #             y=1200, w=1651, h=1200, alpha=0.3)
    img = Image.open(workpath + '/06_Hamburg_S1.jpg')

    fig = go.Figure(go.Histogram2dContour(
        x=x,
        y=y,
        colorscale='Blues'
    ))

    fig.update_layout(
        autosize=False,
        width=700,
        height=600,
        #  margin=dict(
        #      l=50,
        #      r=50,
        #      b=100,
        #      t=100,
        #      pad=4
        #  )
    )
    fig.add_layout_image(
        dict(
            # source=img,
            source='https://i.ibb.co/VQSkMnN/06-Hamburg-S1.jpg',
            xref="x",
            yref="y",
            x=0,
            y=0,
            sizex=500,
            sizey=300,
            sizing="contain",
            opacity=0.7,
            visible=True,
            layer="below")
    )

    fig2 = go.Figure(go.Histogram2dContour(
        x=z,
        y=w,
        colorscale='Blues'
    ))

    fig2.update_layout(
        autosize=False,
        width=700,
        height=600,
        #  margin=dict(
        #      l=50,
        #      r=50,
        #      b=100,
        #      t=100,
        #      pad=4
        #  )
    )
    fig2.add_layout_image(
        dict(
            # source=img,
            source='https://i.ibb.co/VQSkMnN/06-Hamburg-S1.jpg',
            xref="x",
            yref="y",
            x=0,
            y=0,
            sizex=500,
            sizey=300,
            sizing="contain",
            opacity=0.7,
            visible=True,
            layer="below")
    )
    # fig.show()
    # fig.write_html("file.html")
    # show the results
    # fig.show()
    graph = fig.to_html(full_html=False, default_height=500, default_width=700)
    graph2 = fig2.to_html(
        full_html=False, default_height=500, default_width=700)
    script = ""
    # script, div = components(offline.plot(
    # fig, include_plotlyjs=True, output_type='div'))
    # context = {
    #     'age': 22,
    #     'name': 'Tarik'
    # }
    return render(request, 'website_boxplot.html',
                  {'script': script, 'div': graph, 'div2': graph2})
