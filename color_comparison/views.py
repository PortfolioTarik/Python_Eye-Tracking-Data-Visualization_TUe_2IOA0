# Generated en coded by Tarik Hacialiogullari except when noted.
from django.shortcuts import render

from django.http import HttpResponse

from bokeh.embed import components
from bokeh.layouts import row, gridplot

from homepage.models import getUserData, getAllStimulis, getAllUsersByStimuliAndColor, getPreUserByColor, getPreUserByColorAndStimuli

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


def home(request):
    toolbar = "box_select, lasso_select, wheel_zoom, pan, reset, save, hover, help"
    df_userOne = getPreUserByColor('color')
    stimuli = df_userOne['StimuliName'].iloc[0]
    df_userTwo = getPreUserByColorAndStimuli('gray', stimuli)
    userColor = df_userOne['user'].iloc[0]
    userGray = df_userTwo['user'].iloc[0]
    userContour = 'color'
    brev = False

    if request.GET.get('stimuli') is not None:
        stimuli = request.GET['stimuli']
        print('STIMULI IS RECEIVED:' + stimuli)

    #color and gray user from url param.
    if request.GET.get('userColor') is not None:
        userColor = request.GET['userColor']
        print('USERCOLOR IS RECEIVED:' + userColor)
    
    if request.GET.get('userGray') is not None:
        userGray = request.GET['userGray']
        print('USERGRAY IS RECEIVED:' + userGray)
    
    if request.GET.get('userContour') is not None:
        userContour = request.GET['userContour']
        print('USERCONTOUR IS RECEIVED:' + userContour)

    #same as stimuli but for barchart so that you can reverse it order.
    if request.GET.get('brev') is not None:
        brev = parseToBool(request.GET['brev'].lower())
        print('BREV IS RECEIVED:' + str(brev))


    #getData
    df_userOne = getUserData(userColor, stimuli, 'color')
    df_userTwo = getUserData(userGray, stimuli, 'gray')
    userOne_exist = False
    userTwo_exist = False
    if len(df_userOne) > 0:
        userOne_exist = True
    if len(df_userTwo) > 0:
        userTwo_exist = True
    #df_userThree = getUserData('p12', stimuliMap)

    # ---Start Coding by Fanni Egresits
    #GetBackground images
    url = '/static/stimuli/{}'.format(stimuli)
    img_url = "http://" + request.get_host() + url

        #Get the parameters of map (width, height)
    response = requests.get(img_url)
    w, h = Image.open(BytesIO(response.content)).size
    # ---End Coding by Fanni Egresits

    #BOKEH

        #Get Bar graph
    end = len(df_userOne.index) + len(df_userTwo.index)+ 1000
    #end = len(df_userOne.index) + 1000
    graph_bar = getGraphBar(toolbar, end)
    if userOne_exist:
        addUserToGraphBar(df_userOne, graph_bar, 'red', 0, brev)
    if userTwo_exist:
        addUserToGraphBar(df_userTwo, graph_bar, 'yellow', len(df_userOne.index), brev)
    #addUserToGraphBar(df_userThree, graph_bar, 'blue', len(df_userOne.index) + len(df_userTwo.index))
    

        #Get Line graph
    graph_line = getGraphLine(toolbar)
    if userOne_exist:
        addUserToGraphLine(df_userOne, graph_line, 'red')
    if userTwo_exist:
        addUserToGraphLine(df_userTwo, graph_line, 'yellow')
    #addUserToGraphLine(df_userThree, graph_line, 'blue')
    
        #Get Gaze graph
    graph_gaze = getGraphGaze(toolbar, url, w, h)
    if userOne_exist:
        addUserToGraphGaze(df_userOne, graph_gaze, 'red')
    if userTwo_exist:
        addUserToGraphGaze(df_userTwo, graph_gaze, 'yellow')
    #addUserToGraphGaze(df_userThree, graph_gaze, 'blue')

    

        #Convert to HTML
    script_bokeh, graphs_bokeh = components(gridplot([graph_line,  graph_gaze],ncols=2, sizing_mode="scale_both"))
    script_bar, graph_bar = components(graph_bar)
    #script_gaze, script_line, graph_gaze, graph_line = components(gridplot([graph_line, graph_gaze], ncols=2, sizing_mode="scale_both"))
    
    #PLOTLY
    graph_contour = ''
    if userOne_exist and userContour.lower() == 'color':
        graph_contour = getGraphContour(df_userOne, url, w, h)
    elif userTwo_exist and userContour.lower() == 'gray':
        graph_contour = getGraphContour(df_userTwo, url, w, h)
        
    #Stimuli dropdown
    stimuli_list = getAllStimulis()
    user_list_color = getAllUsersByStimuliAndColor(stimuli, 'color')
    user_list_gray = getAllUsersByStimuliAndColor(stimuli, 'gray')

    context = {
        'selected_stimuli': stimuli,
        'selected_userColor': userColor,
        'selected_userGray': userGray,
        'selected_color': userContour.lower(),
        'stimuli_list': stimuli_list,
        'user_list_gray': user_list_gray,
        'user_list_color': user_list_color,
        'graph_contour': graph_contour,
        'graphs_bokeh': graphs_bokeh,
        'graph_bar': graph_bar,
        'graph_line': graph_line,
        'graph_gaze': graph_gaze,
        'script_bokeh' : script_bokeh,
        'script_bar' : script_bar
    }
    return render(request, 'color.html', context)

#Function from https://stackoverflow.com/a/53287252/4641129 to convert text content to boolean type. (only changed the function name)
def parseToBool(string):
    d = {'true': True, 'false': False}
    return d.get(string, string)