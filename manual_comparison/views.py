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

#Some of them are for background not sure which one, just putting all in it m8.
import eye_tracking_visualizations_group23a.settings
from PIL import Image
import requests
from io import BytesIO
from django.contrib.staticfiles.storage import staticfiles_storage

#SEE homepage/views.py for the comments
def home(request):
    toolbar = "box_select, lasso_select, wheel_zoom, pan, reset, save, hover, help"

    stimuli = '06_Hamburg_S1.jpg'
    user = 'p1'
    color = 'color'
    brev = False
    graph = 'gaze'

    if request.GET.get('stimuli') is not None:
        stimuli = request.GET['stimuli']
        print('STIMULI IS RECEIVED:' + stimuli)

    if request.GET.get('user') is not None:
        user = request.GET['user']
        print('USER IS RECEIVED:' + user)

    if request.GET.get('color') is not None:
        color = request.GET['color']
        print('COLOR IS RECEIVED:' + color)
    
    #same as stimuli but for barchart so that you can reverse it order.
    if request.GET.get('brev') is not None:
        brev = parseToBool(request.GET['brev'].lower())
        print('BREV IS RECEIVED:' + str(brev))

    # Coded by Laura
    if request.GET.get('graph') is not None:
        graph = request.GET['graph']
        print('GRAPH IS RECEIVED' + graph)
        # end coding Laura

    #getData
    df_userOne = getUserData(user, stimuli, color)

    # ---Start Coding by Fanni Egresits
    #GetBackground images
    url = '/static/stimuli/{}'.format(stimuli)
    img_url = "http://" + request.get_host() + url

        #Get the parameters of map (width, height)
    response = requests.get(img_url)
    w, h = Image.open(BytesIO(response.content)).size
    # ---End Coding by Fanni Egresits

    selected_graph = 0

    # Coded by Fanni and Laura
    if graph == 'gaze':
        selected_graph = getGraphGaze(toolbar, url, w, h)
        addUserToGraphGaze(df_userOne, selected_graph, 'red')
        script_graph, selected_graph = components(selected_graph)
    elif graph == 'line':
        selected_graph = getGraphLine(toolbar)
        addUserToGraphLine(df_userOne, selected_graph, 'red')
        script_graph, selected_graph = components(selected_graph)
    elif graph == 'bar':
        end = len(df_userOne.index) + 1000
        selected_graph = getGraphBar(toolbar, end)
        addUserToGraphBar(df_userOne, selected_graph, 'red', 0, brev)
        script_graph, selected_graph = components(selected_graph)
    elif graph == 'contour':
        selected_graph = getGraphContour(df_userOne, url, w, h)
        script_graph = 0
        #end coding Fanni and Laura

    #Stimuli dropdown
    stimuli_list = getAllStimulis()
    user_list = getAllUsersByStimuli(stimuli)
    graph_list = {'gaze', 'contour', 'bar', 'line'}

    #Updated from homepage context by Fanni and Laura
    context = {
        'graph_selected' : selected_graph,
        'graphselection' : graph,
        'selected_stimuli': stimuli,
        'selected_user': user,
        'selected_color': color,
        'stimuli_list': stimuli_list,
        'user_list': user_list,
        'script_graph': script_graph,
        'graph_list' : graph_list,
    }
    return render(request, 'manual.html', context)

#Function from https://stackoverflow.com/a/53287252/4641129 to convert text content to boolean type. (only changed the function name)
def parseToBool(string):
    d = {'true': True, 'false': False}
    return d.get(string, string)