from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file
import os
from bokeh.layouts import row


def home(request):

    workpath = os.path.dirname(os.path.abspath(__file__))
    # path is '/csv/all_fixation_data_cleaned_up.csv'
    df_eye = pd.read_csv(
        workpath + '/csv/all_fixation_data_cleaned_up.csv', encoding='unicode_escape', sep="\t")

    # copy dataset with specialized columns (just for testing something)
    df_eye_test = df_eye[['user', 'StimuliName']].copy()

    # Using the data for x axis Timestamp and y axis time duration to see time spent per point
    x = df_eye[(df_eye_test['StimuliName'] == '06_Hamburg_S1.jpg') &
               (df_eye_test['user'] == 'p1')]["Timestamp"]
    y = df_eye[(df_eye_test['StimuliName'] == '06_Hamburg_S1.jpg') &
               (df_eye_test['user'] == 'p1')]["FixationDuration"]
    print(x)

    # output to static HTML file
    # output_file("lines.html")

    # create a new plot with a title and axis labels
    p1 = figure(plot_width=600, plot_height=400, x_range=(38000, 43000), y_range=(100, 700),
                title="Fixation Duration per point for color", x_axis_label='Timestamp',
                y_axis_label='FixationDuration')

    # add a line renderer with legend and line thickness
    p1.line(x, y, legend_label="P1.", line_width=2, color="red")
    p1.circle(x, y, fill_color="black",
              color="red", size=6)
# Another Line Chart to compare two users of color and gray
    # copy dataset with specialized columns (just for testing something)
    df_eye_test_2 = df_eye[['user', 'StimuliName']].copy()

    # Using the data for x axis Timestamp and y axis time duration to see time spent per point
    a = df_eye[(df_eye_test_2['StimuliName'] == '06b_Hamburg_S2.jpg') &
               (df_eye_test_2['user'] == 'p9')]["Timestamp"]
    b = df_eye[(df_eye_test_2['StimuliName'] == '06b_Hamburg_S2.jpg') &
               (df_eye_test_2['user'] == 'p9')]["FixationDuration"]
    print(x)

    # output to static HTML file
    # output_file("lines.html")

    # create a new plot with a title and axis labels
    p2 = figure(plot_width=600, plot_height=400, x_range=(190000, 202000), y_range=(100, 700),
                title="Fixation Duration per point for gray", x_axis_label='Timestamp',
                y_axis_label='FixationDuration')

    # add a line renderer with legend and line thickness
    p2.line(a, b, legend_label="P9.", line_width=2, color="red")
    p2.circle(a, b, fill_color="black",
              color="red", size=6)
    # For layout
    #show(row(p1, p2))

    # show the results
    script, div = components(row(p1, p2))
    context = {
        'age': 18,
        'name': 'Omar'
    }
    return render(request, 'website_starplot.html',
                  {'script': script, 'div': div})
