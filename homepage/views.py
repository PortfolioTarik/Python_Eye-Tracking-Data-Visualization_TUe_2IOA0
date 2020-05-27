# Generated en coded by Tarik Hacialiogullari except when noted.
from django.shortcuts import render

from django.http import HttpResponse

from bokeh.embed import components
from bokeh.layouts import row, gridplot

from homepage.models import getUserData

from visualization_heatmap.views import getGraph as getGraphContour

from visualization_gazeplot.views import getGraph as getGraphGaze
from visualization_gazeplot.views import addUserToGraph as addUserToGraphGaze

from visualization_barchart.views import getGraph as getGraphBar
from visualization_barchart.views import addUserToGraph as addUserToGraphBar

from visualization_linechart.views import getGraph as getGraphLine
from visualization_linechart.views import addUserToGraph as addUserToGraphLine

webpages = [
    {
        'title': 'Import_csv',
        'url': '/import'
    },
]

def home(request):
    toolbar = "box_select, lasso_select, wheel_zoom, pan, reset, save, hover, help"

    #getData
    df_userOne = getUserData('p1', '06_Hamburg_S1.jpg')
    df_userTwo = getUserData('p16', '06_Hamburg_S1.jpg')
    df_userThree = getUserData('p12', '06_Hamburg_S1.jpg')

    #BOKEH

        #Get Bar graph
    end = len(df_userOne.index) + len(df_userTwo.index)+ 1000
    graph_bar = getGraphBar(toolbar, end)
    addUserToGraphBar(df_userOne, graph_bar, 'red', 0)
    addUserToGraphBar(df_userTwo, graph_bar, 'yellow', len(df_userOne.index))
    addUserToGraphBar(df_userThree, graph_bar, 'blue', len(df_userOne.index) + len(df_userTwo.index))
        #Get Line graph
    graph_line = getGraphLine(toolbar)
    addUserToGraphLine(df_userOne, graph_line, 'red')
    addUserToGraphLine(df_userTwo, graph_line, 'yellow')
    addUserToGraphLine(df_userThree, graph_line, 'blue')
    
        #Get Gaze graph
    graph_gaze = getGraphGaze(toolbar)
    addUserToGraphGaze(df_userOne, graph_gaze, 'red')
    addUserToGraphGaze(df_userTwo, graph_gaze, 'yellow')
    addUserToGraphGaze(df_userThree, graph_gaze, 'blue')

        #Convert to HTML
    script_bokeh, graphs_bokeh = components(gridplot([graph_line, graph_bar, graph_gaze], ncols=2, sizing_mode="scale_both"))

    #PLOTLY
    graphs_plotly = getGraphContour(df_userOne)

    context = {
        'webpages': webpages,
        'graphs_plotly': graphs_plotly,
        'graphs_bokeh': graphs_bokeh,
        'script_bokeh' : script_bokeh
    }
    return render(request, 'home.html', context)