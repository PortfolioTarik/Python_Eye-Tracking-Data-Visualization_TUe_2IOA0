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


def home(request):
    workpath = os.path.dirname(os.path.abspath(__file__))
    df = pd.read_csv(workpath +
                     '/all_fixation_data_cleaned_up.csv', encoding='unicode_escape', sep="\t")

    # copy dataset with specialized columns (just for testing something)
    test = df[['user', 'StimuliName']].copy()
    # print(test[(test['StimuliName'] == '07_Moskau_S1.jpg') & (test['user'] == 'p1')])

    # print(test[test['user'] == "p2"] & test[test['StimuliName'] == "07_Moskau_S1.jpg"])
    # prepare some data 3 criteria
    userData = df[(test['StimuliName'] == '06_Hamburg_S1.jpg')
                  & (test['user'] == 'p1')]
    x = df[(test['StimuliName'] == '06_Hamburg_S1.jpg') &
           (test['user'] == 'p1')]["MappedFixationPointX"]
    y = df[(test['StimuliName'] == '06_Hamburg_S1.jpg') &
           (test['user'] == 'p1')]["MappedFixationPointY"]
    z = df[(test['StimuliName'] == '06b_Hamburg_S2.jpg') &
           (test['user'] == 'p16')]["MappedFixationPointX"]
    w = df[(test['StimuliName'] == '06b_Hamburg_S2.jpg') &
           (test['user'] == 'p16')]["MappedFixationPointY"]

    # output to static HTML file
    # output_file("lines.html")

    # create a new plot with a title and axis labels
    p = figure(plot_width=800, plot_height=600, x_range=(0, 1651), y_range=(0, 1200),
               title="Gaze plot of Hamburg of the first user", x_axis_label='Mapped Fixation Point X',
               y_axis_label='Mapped Fixation Point Y')

    p.image_url(url=[
        'https://i.ibb.co/VQSkMnN/06-Hamburg-S1.jpg'], x=0, y=1200, w=1651, h=1200)

    # add a line renderer with legend and line thickness
    p.line(x, y, legend_label="P1.", line_width=2, color="red")
    p.line(z, w, legend_label="P16.", line_width=2, color="blue")
    # count = 0
#     for hor in x:
#         ver = y.iloc[count]
#         count = count + 1
#         print('x= ' + str(hor) + ' ver= ' + str(ver))
#         p.circle(hor, ver, fill_color="red",
#                  color="red", size=8)
    sizePath = x.count()
    numericalArr = list(range(1, sizePath + 1))
    fixDur = userData['FixationDuration']
    fixationDurationArr = [fixDur.iloc[[i]] /
                           15 for i in list(range(0, sizePath))]
    # numericalArr = [str(i) for i in list(range(1, sizePath))]

    source = ColumnDataSource(data=dict(height=y,
                                        weight=x,
                                        names=numericalArr,
                                        fixationDuration=fixationDurationArr))
#     count = 0
#     for index, row in userData.iterrows():
    # p.circle(row['MappedFixationPointX'], row['MappedFixationPointY'],
    #         fill_color="black", color="red", size=row['FixationDuration']/15, name='len')
    #  p.add_layout(Label(x=row['MappedFixationPointX'], y=row['MappedFixationPointY'], text=str(count), level='glyph',
    #                     x_offset=5, y_offset=5, render_mode='canvas'))
    #  count = count + 1
    p.circle('weight', 'height', fill_color="black",
             color="red", size='fixationDuration', source=source)
    # p.circle(x, y, fill_color="red",
    # color="red", size=8)

    # x.head()
    p.add_layout(LabelSet(x='weight', y='height', text='names', level='overlay',
                          x_offset=5, y_offset=5, text_color="red", source=source, render_mode='canvas'))
    # add background

    # show the results
    script, div = components(p)
    return render(request, 'website_starplot.html',
                  {'script': script, 'div': div})
