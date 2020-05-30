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


def home(request):
    #Standard toolbar (on the right / above) for every graph.
    toolbar = "box_select, lasso_select, wheel_zoom, pan, reset, save, hover, help"
    #Pre-data (always these 3 options are selected when opening website)
    stimuli = '06_Hamburg_S1.jpg'
    user = 'p1'
    color = 'color'

    #If there is a stimuli in the URL like '?stimuli=istanbul.jpg' then overwrite the pre-data of above and put that in.
    if request.GET.get('stimuli') is not None:
        stimuli = request.GET['stimuli']
        print('STIMULI IS RECEIVED:' + stimuli)
    #same as stimuli but for user
    if request.GET.get('user') is not None:
        user = request.GET['user']
        print('USER IS RECEIVED:' + user)
    #same as stimuli but for color
    if request.GET.get('color') is not None:
        color = request.GET['color']
        print('COLOR IS RECEIVED:' + color)


    #Take the selected user (by stimuli and color) from the database.
    df_userOne = getUserData(user, stimuli, color)

    #BOKEH
        #Get Bar graph
    #Don't touch this end variable it provides the amount of label text needed on the x-axis of bar graph.
    end = len(df_userOne.index) + 1000
    #Get the bar graph figure from visualization_barchart/views.py
    graph_bar = getGraphBar(toolbar, end)
    #Add just one user to the bar graph with color red.
    addUserToGraphBar(df_userOne, graph_bar, 'red', 0)
    

        #Get Line graph
    #Get the line graph figure from visualization_linegraph/views.py
    graph_line = getGraphLine(toolbar)
    #Add just one user to the line graph with color red.
    addUserToGraphLine(df_userOne, graph_line, 'red')
    
        #Get Gaze graph
    #Get the gaze graph figure from visualization_gazeplot/views.py also send the current stimuli which is selected, so it generate this graph with this background.
    graph_gaze = getGraphGaze(toolbar, stimuli, request)
    addUserToGraphGaze(df_userOne, graph_gaze, 'red')

        #Convert the BAR, LINE, GAZE plot to HTML (So only the Bokeh plots)
    script_bokeh, graphs_bokeh = components(gridplot([graph_line,  graph_gaze],ncols=2, sizing_mode="scale_both"))
    script_bar, graph_bar = components(graph_bar)
    
    #PLOTLY
    #get the contour map from 'visualization_heatmap/views.py' for the one user we have retrieved.
    graph_contour = getGraphContour(df_userOne)

    #Stimuli dropdown
    #Get all the stimulis in order to send it with context to the homepage.
    stimuli_list = getAllStimulis()
    #Get all the users which are on this stimuli.
    user_list = getAllUsersByStimuli(stimuli)

    #the array that we send to the homepage.
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
    #return the home.html to the requester with the contect array in it rendered.
    return render(request, 'home.html', context)