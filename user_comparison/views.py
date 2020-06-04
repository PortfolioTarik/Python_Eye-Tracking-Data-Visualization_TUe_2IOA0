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


#SEE homepage/views.py for the comments, except for multiple users section.
def home(request):
    toolbar = "box_select, lasso_select, wheel_zoom, pan, reset, save, hover, help"

    stimuli = '06_Hamburg_S1.jpg'
    users = ['p1']
    color = 'color'
    amountOfUsers = 1
    

    if request.GET.get('stimuli') is not None:
        stimuli = request.GET['stimuli']
        print('STIMULI IS RECEIVED:' + stimuli)

    if request.GET.get('user') is not None:
        users = request.GET.getlist('user')
        #collect all the users which is selected (from URL params) and make a String list of them.
        users = list(dict.fromkeys(users))
        print('USERS ARE RECEIVED:')
        print(users)
        amountOfUsers = len(users)
        

    if request.GET.get('color') is not None:
        color = request.GET['color']
        print('COLOR IS RECEIVED:' + color)

    
    #getData
    #We can get already the first selected user.
    df_userOne = getUserData(users[0], stimuli, color)
    df_userTwo = ''
    df_userThree = ''
    #With booleans it is easy to see how many users there are, it is more optimal compared to everytime array look up.
    boolUserTwo = False
    boolUserThree = False
    #Determine how many users we have and retrieve 3 of them.
    if(amountOfUsers >= 2):
        boolUserTwo = True
        df_userTwo = getUserData(users[1], stimuli, color)
    if(amountOfUsers >= 3):
        boolUserThree = True
        df_userThree = getUserData(users[2], stimuli, color)

    #BOKEH
        #Get Bar graph
    end = len(df_userOne.index) + 1000
    if boolUserThree:
        end = len(df_userOne.index) + len(df_userTwo.index)+ 1000
    graph_bar = getGraphBar(toolbar, end)
    addUserToGraphBar(df_userOne, graph_bar, 'red', 0)
    #if there is also selected an User two show it.
    if boolUserTwo:
        addUserToGraphBar(df_userTwo, graph_bar, 'yellow', len(df_userOne.index))
    #if there is also selected an User three show it also.
    if boolUserThree:
        addUserToGraphBar(df_userThree, graph_bar, 'blue', len(df_userOne.index) + len(df_userTwo.index))
    

        #Get Line graph
    graph_line = getGraphLine(toolbar)
    addUserToGraphLine(df_userOne, graph_line, 'red')
    if boolUserTwo:
        addUserToGraphLine(df_userTwo, graph_line, 'yellow')
    if boolUserThree:
        addUserToGraphLine(df_userThree, graph_line, 'blue')
    
        #Get Gaze graph
    graph_gaze = getGraphGaze(toolbar, stimuli, request)
    addUserToGraphGaze(df_userOne, graph_gaze, 'red')
    if boolUserTwo:
        addUserToGraphGaze(df_userTwo, graph_gaze, 'yellow')
    if boolUserThree:
        addUserToGraphGaze(df_userThree, graph_gaze, 'blue')

    

        #Convert to HTML
    script_bokeh, graphs_bokeh = components(gridplot([graph_line,  graph_gaze],ncols=2, sizing_mode="scale_both"))
    script_bar, graph_bar = components(graph_bar)
    
    #PLOTLY
    graph_contour = getGraphContour(df_userOne, stimuli, request)

    #Stimuli dropdown
    stimuli_list = getAllStimulis()
    user_list = getAllUsersByStimuli(stimuli)

    context = {
        'selected_stimuli': stimuli,
        'selected_users': users,
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
    return render(request, 'user.html', context)