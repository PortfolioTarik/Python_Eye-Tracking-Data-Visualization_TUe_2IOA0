# Generated en coded by Tarik Hacialiogullari except where noted.
from django.shortcuts import render

from django.http import HttpResponse

from bokeh.embed import components
from bokeh.layouts import row, gridplot

from homepage.models import getUserData, getAllStimulis, getAllUsersByStimuli

from visualization_heatmap.views import getGraph as getGraphContour

from visualization_gazeplot.views import getGraph as getGraphGaze
from visualization_gazeplot.views import addUserToGraph as addUserToGraphGaze

from visualization_barchart.views import getGraph as getGraphBar
from visualization_barchart.views import addUserToGraph as addUserToGraphBar

from visualization_linechart.views import getGraph as getGraphLine
from visualization_linechart.views import addUserToGraph as addUserToGraphLine

#SEE homepage/views.py for the comments
def home(request):
    toolbar = "box_select, lasso_select, wheel_zoom, pan, reset, save, hover, help"

    stimuli = '06_Hamburg_S1.jpg'
    user = 'p1'
    color = 'color'

    if request.GET.get('stimuli') is not None:
        stimuli = request.GET['stimuli']
        print('STIMULI IS RECEIVED:' + stimuli)

    if request.GET.get('user') is not None:
        user = request.GET['user']
        print('USER IS RECEIVED:' + user)

    if request.GET.get('color') is not None:
        color = request.GET['color']
        print('COLOR IS RECEIVED:' + color)


    #getData
    df_userOne = getUserData(user, stimuli, color)
    #df_userTwo = getUserData('p16', stimuliMap)
    #df_userThree = getUserData('p12', stimuliMap)

    #BOKEH

        #Get Bar graph
    #end = len(df_userOne.index) + len(df_userTwo.index)+ 1000
    end = len(df_userOne.index) + 1000
    graph_bar = getGraphBar(toolbar, end)
    addUserToGraphBar(df_userOne, graph_bar, 'red', 0)
    #addUserToGraphBar(df_userTwo, graph_bar, 'yellow', len(df_userOne.index))
    #addUserToGraphBar(df_userThree, graph_bar, 'blue', len(df_userOne.index) + len(df_userTwo.index))
    

        #Get Line graph
    graph_line = getGraphLine(toolbar)
    addUserToGraphLine(df_userOne, graph_line, 'red')
    #addUserToGraphLine(df_userTwo, graph_line, 'yellow')
    #addUserToGraphLine(df_userThree, graph_line, 'blue')
    
        #Get Gaze graph
    graph_gaze = getGraphGaze(toolbar, stimuli)
    addUserToGraphGaze(df_userOne, graph_gaze, 'red')
    #addUserToGraphGaze(df_userTwo, graph_gaze, 'yellow')
    #addUserToGraphGaze(df_userThree, graph_gaze, 'blue')

    

        #Convert to HTML
    script_bokeh, graphs_bokeh = components(gridplot([graph_line,  graph_gaze],ncols=2, sizing_mode="scale_both"))
    #script_bars = script_bar
    script_bar, graph_bar = components(graph_bar)
    #script_gaze, script_line, graph_gaze, graph_line = components(gridplot([graph_line, graph_gaze], ncols=2, sizing_mode="scale_both"))
    
    #PLOTLY
    graph_contour = getGraphContour(df_userOne)

    #Stimuli dropdown
    stimuli_list = getAllStimulis()
    user_list = getAllUsersByStimuli(stimuli)


    context = {
        'selected_stimuli': stimuli,
        'selected_user': user,
        'selected_color': color,
        'stimuli_list': stimuli_list,
        'user_list': user_list,
        'graph_contour': graph_contour,
        'graphs_bokeh': graphs_bokeh,
        'graph_bar': graph_bar,
        'graph_line': graph_line,
        'graph_gaze': graph_gaze,
        'script_bokeh' : script_bokeh,
        'script_bar' : script_bar
    }
    return render(request, 'manual.html', context)