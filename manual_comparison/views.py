# Generated en coded by Tarik Hacialiogullari except where noted.
from django.shortcuts import render

from django.http import HttpResponse

from bokeh.embed import components
from bokeh.layouts import row, gridplot

from homepage.models import getUserData, getAllStimulis, getAllUsersByStimuliAndColor, getPreUserByColor

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
    barchart_width = 685
    barchart_height = 510
    linechart_width = 685
    linechart_height = 510
    percent = 85

    df_userLeft = getPreUserByColor('color')
    stimuli_left = df_userLeft['StimuliName'].iloc[0]
    user_left = df_userLeft['user'].iloc[0]
    color_left = df_userLeft['description'].iloc[0]
    brev_left = False
    graph_left = 'gaze'

    df_userRight = getPreUserByColor('color')
    stimuli_right = df_userRight['StimuliName'].iloc[0]
    user_right =  df_userRight['user'].iloc[0]
    color_right = df_userRight['description'].iloc[0]
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

    # getData
    df_userLeft = getUserData(user_left, stimuli_left, color_left)
    df_userRight = getUserData(user_right, stimuli_right, color_right)

    #each graph own users regarding their selected options.
    user_list_left = getAllUsersByStimuliAndColor(stimuli_left, color_left)
    user_list_right = getAllUsersByStimuliAndColor(stimuli_right, color_right)

    print(len(df_userLeft))
    if len(df_userLeft) <= 0:
        print("UserLeft doesn't exists: " + user_left + "for this map, so we switched to another user :)")
        user_left = user_list_left[0]
        df_userLeft = getUserData(user_left, stimuli_left, color_left)
        print(len(df_userLeft))

    if len(df_userRight) <= 0:
        print("UserLeft doesn't exists: " + user_right + "for this map, so we switched to another user :)")
        user_right = user_list_right[0]
        df_userRight = getUserData(user_right, stimuli_right, color_right)

    # ---Start Coding by Fanni Egresits
    # GetBackground images
    url_left = '/static/stimuli/{}'.format(stimuli_left)
    img_url_left = "http://" + request.get_host() + url_left
    url_right = '/static/stimuli/{}'.format(stimuli_right)
    img_url_right = "http://" + request.get_host() + url_right
    

    # Get the parameters of map (width, height)
    response_left = requests.get(img_url_left)
    w_left, h_left = Image.open(BytesIO(response_left.content)).size
    response_right = requests.get(img_url_right)
    w_right, h_right = Image.open(BytesIO(response_right.content)).size
    #w_right = (w_right/100) *70
    
    # ---End Coding by Fanni Egresits


    # Coded by Fanni and Laura
    selected_graph_left = 0
    script_graph_left = 0
    if graph_left == 'gaze':
        selected_graph_left = getGraphGaze(toolbar, url_left, w_left, h_left, percent)
        addUserToGraphGaze(df_userLeft, selected_graph_left, 'red')
        script_graph_left , selected_graph_left = components(selected_graph_left)
    elif graph_left == 'line':
        selected_graph_left = getGraphLine(toolbar, linechart_width, linechart_height)
        addUserToGraphLine(df_userLeft, selected_graph_left, 'red')
        script_graph_left , selected_graph_left = components(selected_graph_left)
    elif graph_left == 'bar':
        end = len(df_userLeft.index) + 1000
        selected_graph_left = getGraphBar(toolbar, end, barchart_width, barchart_height)
        addUserToGraphBar(df_userLeft, selected_graph_left, 'red', 0, brev_left)
        script_graph_left , selected_graph_left = components(selected_graph_left)
    elif graph_left == 'contour':
        selected_graph_left = getGraphContour(df_userLeft, url_left, w_left, h_left, percent)

    selected_graph_right = 0
    script_graph_right = 0
    if graph_right == 'gaze':
        selected_graph_right = getGraphGaze(toolbar, url_right, w_right, h_right, percent)
        addUserToGraphGaze(df_userRight, selected_graph_right, 'red')
        script_graph_right , selected_graph_right = components(selected_graph_right)
    elif graph_right == 'line':
        selected_graph_right = getGraphLine(toolbar, linechart_width, linechart_height)
        addUserToGraphLine(df_userRight, selected_graph_right, 'red')
        script_graph_right , selected_graph_right = components(selected_graph_right)
    elif graph_right == 'bar':
        end = len(df_userRight.index) + 1000
        selected_graph_right = getGraphBar(toolbar, end, barchart_width, barchart_height)
        addUserToGraphBar(df_userRight, selected_graph_right, 'red', 0, brev_right)
        script_graph_right , selected_graph_right = components(selected_graph_right)
    elif graph_right == 'contour':
        selected_graph_right = getGraphContour(df_userRight, url_right, w_right, h_right, percent)

        # end coding Fanni and Laura

    # Stimuli dropdown
    stimuli_list = getAllStimulis()
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
        'selected_stimuli_left': stimuli_left,
        'selected_stimuli_right': stimuli_right,
        'selected_user_left': user_left,
        'selected_user_right': user_right,
        'selected_color_left': color_left,
        'selected_color_right': color_right,
        'stimuli_list': stimuli_list,
        'user_list_left': user_list_left,
        'user_list_right': user_list_right,
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

