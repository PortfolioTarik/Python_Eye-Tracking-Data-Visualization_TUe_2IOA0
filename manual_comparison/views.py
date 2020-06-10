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

# Some of them are for background not sure which one, just putting all in it m8.
import eye_tracking_visualizations_group23a.settings
from PIL import Image
import requests
from io import BytesIO
from django.contrib.staticfiles.storage import staticfiles_storage


# SEE homepage/views.py for the comments
def home(request):
    toolbar = "box_select, lasso_select, wheel_zoom, pan, reset, save, hover, help"

    # stimuli has to be the same for left
    stimuli_left = '06_Hamburg_S1.jpg'
    user_left = 'p1'
    color_left = 'color'
    brev_left = False
    graph_left = 'gaze'

    stimuli_right = '06_Hamburg_S1.jpg'
    user_right = 'p1'
    color_right = 'color'
    brev_right = False
    graph_right = 'gaze'

    if request.GET.get('stimuli_left') is not None:
        stimuli_left = request.GET['stimuli_left']
        print('STIMULI_LEFT IS RECEIVED:' + stimuli_left)
    
    if request.GET.get('stimuli_right') is not None:
        stimuli_right = request.GET['stimuli_right']
        print('STIMULI_RIGHT IS RECEIVED:' + stimuli_right)

    if request.GET.get('user_left') is not None:
        user_left = request.GET['user_left']
        print('USER IS RECEIVED:' + user_left)
    if request.GET.get('user_right') is not None:
        user_right = request.GET['user_right']
        print('USER IS RECEIVED:' + user_right)

    if request.GET.get('color_left') is not None:
        color_left = request.GET['color_left']
        print('COLOR IS RECEIVED:' + color_left)
    if request.GET.get('color_right') is not None:
        color_right = request.GET['color_right']
        print('COLOR IS RECEIVED:' + color_right)

    # Coded by Laura
    if request.GET.get('graph_left') is not None:
        graph_left = request.GET['graph_left']
        print('GRAPH IS RECEIVED' + graph_left)
    if request.GET.get('graph_right') is not None:
        graph_right = request.GET['graph_right']
        print('GRAPH IS RECEIVED' + graph_right)
        # end coding Laura
 #REMOVE ME ------------------------------------------------------- TEMPORARY----------------------------
    #I didn't see any stimuli_left and stimuli_right I have made it enabeld to retrieve stimuli_left and stimuli_right
    #it is up to the one who is responsible for the task to implemend it.
    #So for now I do assign this.
    stimuli = stimuli_left
#REMOVE ME ------------------------------------------------------- TEMPORARY-----------------------------
    # getData
    df_userLeft = getUserData(user_left, stimuli, color_left)
    df_userRight = getUserData(user_right, stimuli, color_right)

    # ---Start Coding by Fanni Egresits
    # GetBackground images
    url = '/static/stimuli/{}'.format(stimuli)
    img_url = "http://" + request.get_host() + url

    # Get the parameters of map (width, height)
    response = requests.get(img_url)
    w, h = Image.open(BytesIO(response.content)).size
    # ---End Coding by Fanni Egresits

    # Coded by Fanni and Laura
    selected_graph_left = 0
    script_graph_left = 0
    if graph_left == 'gaze':
        selected_graph_left = getGraphGaze(toolbar, url, w, h)
        addUserToGraphGaze(df_userLeft, selected_graph_left, 'red')
        script_graph_left , selected_graph_left = components(selected_graph_left)
    elif graph_left == 'line':
        selected_graph_left = getGraphLine(toolbar)
        addUserToGraphLine(df_userLeft, selected_graph_left, 'red')
        script_graph_left , selected_graph_left = components(selected_graph_left)
    elif graph_left == 'bar':
        end = len(df_userLeft.index) + 1000
        selected_graph_left = getGraphBar(toolbar, end)
        addUserToGraphBar(df_userLeft, selected_graph_left, 'red', 0, brev_left)
        script_graph_left , selected_graph_left = components(selected_graph_left)
    elif graph_left == 'contour':
        selected_graph_left = getGraphContour(df_userLeft, url, w, h)

    selected_graph_right = 0
    script_graph_right = 0
    if graph_right == 'gaze':
        selected_graph_right = getGraphGaze(toolbar, url, w, h)
        addUserToGraphGaze(df_userRight, selected_graph_right, 'red')
        script_graph_right , selected_graph_right = components(selected_graph_right)
    elif graph_right == 'line':
        selected_graph_right = getGraphLine(toolbar)
        addUserToGraphLine(df_userRight, selected_graph_right, 'red')
        script_graph_right , selected_graph_right = components(selected_graph_right)
    elif graph_right == 'bar':
        end = len(df_userRight.index) + 1000
        selected_graph_right = getGraphBar(toolbar, end)
        addUserToGraphBar(df_userRight, selected_graph_right, 'red', 0, brev_right)
        script_graph_right , selected_graph_right = components(selected_graph_right)
    elif graph_right == 'contour':
        selected_graph_right = getGraphContour(df_userRight, url, w, h)

        # end coding Fanni and Laura

    # Stimuli dropdown
    stimuli_list = getAllStimulis()
    user_list = getAllUsersByStimuli(stimuli)
    graph_list = {'gaze', 'contour', 'bar', 'line'}


    #Convert to HTML
    #script_graph, graph_toCompare = components(gridplot([selected_graph_left, selected_graph_right], ncols=2, sizing_mode="scale_both"))
   # script_bar, graph_bar = components(graph_bar)

    # Updated from homepage context by Fanni and Laura
    context = {
        'selected_graph_left': selected_graph_left,
        'selected_graph_right': selected_graph_right,
        'graph_left': graph_left,
        'graph_right': graph_right,
        'selected_stimuli': stimuli,
        'selected_user_left': user_left,
        'selected_user_right': user_right,
        'selected_color_left': color_left,
        'selected_color_right': color_right,
        'stimuli_list': stimuli_list,
        'user_list': user_list,
        'script_graph_left': script_graph_left,
        'script_graph_right': script_graph_right,
        'graph_list': graph_list

    }
    return render(request, 'manual.html', context)
#'graph_toCompare': graph_toCompare,

# Function from https://stackoverflow.com/a/53287252/4641129 to convert text content to boolean type. (only changed the function name)
def parseToBool(string):
    d = {'true': True, 'false': False}
    return d.get(string, string)

