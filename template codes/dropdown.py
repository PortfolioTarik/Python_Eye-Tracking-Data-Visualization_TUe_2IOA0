import plotly.graph_objects as go

import pandas as pd

# load dataset in each vis
# create figure - in each vis already

# Update plot sizing
#fig.update_layout(
#    autosize=False,
#    width=700,
#    height=600,,
#    margin=dict(t=0, b=0, l=0, r=0),
#)


# Add dropdown
# !! for data changa use UPDATE method, for graph type change use RESTYLE !!
fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=["type", "surface"],
                    label="01_Antwerpen_S1.jpg",
                    method="update"
                ),
                dict(
                    args=["type", "surface"],
                    label="02_Berlin_S1.jpg",
                    method="update"
                ),
                dict(
                    args=["type", "surface"],
                    label="03_Bordeaux_S1.jpg",
                    method="update"
                ),
                dict(
                    args=["type", "surface"],
                    label="04_Kln_S1.jpg",
                    method="update"
                ),
                dict(
                    args=["type", "surface"],
                    label="05_Frankfurt_S1.jpg",
                    method="update"
                ),
                dict(
                    args=["type", "surface"],
                    label="06_Hamburg_S1.jpg",
                    method="update"
                ),
                dict(
                    args=["type", "surface"],
                    label="07_Moskau_S1.jpg",
                    method="update"
                ),
            ]),
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.1,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),
    ]
)

# Add annotation
fig.update_layout(
    annotations=[
        dict(text="Stimuli:", showarrow=False,
        x=0, y=1.085, yref="paper", align="left")
    ]
)

#fig.show()


# with query input
columns = ['ID', 'Timestamp', 'StimuliName', 'FixationIndex', 'FixationDuration',
               'MappedFixationPointX', 'MappedFixationPointY', 'user', 'description']

columns_sql = ', '.join(columns)
fig = go.Figure( layout = layout )

    #---Start Coding by Andrada Pancu
    query_maps = FixationData.objects.raw(
        "SELECT DISTINCT StimuliName, 1 as id FROM Fixation_data ")

    query_users = FixationData.objects.raw(
        "SELECT DISTINCT user, 1 as id FROM Fixation_data ")

    stimuli_list = ["StimuliName:"]
    user_list = ['User:']

    for stimulidata in query_maps: 
        stimuli_list.append(stimulidata.StimuliName)
    
    for userdata in query_users: 
        user_list.append(userdata.user)

    for i in range(1,len(user_list)):
        #if stimuli_list[i] != "StimuliName:":
        bool_visible = False
        if i == 1:
            bool_visible = True
        fig.add_trace(
            go.Histogram2dContour( x = getUserData(user_list[i], stimuli_list[i])["MappedFixationPointX"] ,
                y = getUserData(user_list[i], stimuli_list[i])["MappedFixationPointY"],
                name = stimuli_list[i], visible = bool_visible ))

    fig.update_layout(
        updatemenus=[
            dict(
                buttons=list([
                    dict(
                        args=[{"visible": [True, False, False, False, False, False, False]},
                        {"title": stimuli_list[1],
                        "annotations": []}],
                        label=stimuli_list[1],
                        method="update"
                    ),
                    dict(
                            args=[{"visible": [False, True, False, False, False, False, False]},
                            {"title": stimuli_list[2],
                            "annotations": []}],
                            label=stimuli_list[2],
                            method="update"
                    ),
                    dict(
                            args=[{"visible": [False, False, True, False, False, False, False]},
                            {"title": stimuli_list[3],
                            "annotations": []}],
                            label=stimuli_list[3],
                            method="update"
                    ),
                    dict(
                            args=[{"visible": [False, False, False, True, False, False, False]},
                            {"title": stimuli_list[4],
                            "annotations": []}],
                            label=stimuli_list[4],
                            method="update"
                    ),
                    dict(
                            args=[{"visible": [False, False, False, False, True, False, False]},
                            {"title": stimuli_list[5],
                            "annotations": []}],
                            label=stimuli_list[5],
                            method="update"
                    ),
                    dict(
                            args=[{"visible": [False, False, False, False, False, True, False]},
                            {"title": stimuli_list[6],
                            "annotations": []}],
                            label=stimuli_list[6],
                            method="update"
                    ),
                    dict(
                            args=[{"visible": [False, False, False, False, False, False, True]},
                            {"title": stimuli_list[7],
                            "annotations": []}],
                            label=stimuli_list[7],
                            method="update"
                        ),
                ]),
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.5,
                    xanchor="left",
                    y=1.14,
                    yanchor="top"
            ),
                #---End Coding by Andrada
                #---Start Coding by Fanni Egresits
                dict(
                    buttons=list([
                        dict(
                            args=["colorscale", "Hot"],
                            label="Orange",
                            method="restyle"
                        ),
                        dict(
                            args=["colorscale", "Greys"],
                            label="Grey",
                            method="restyle"
                        ),
                        dict(
                            args=["colorscale", "Greens"],
                            label="Green",
                            method="restyle"
                        ),
                    ]),
                    #---End Coding by Fanni Egresits
                    #---Start Coding by Andrada
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.12,
                    xanchor="left",
                    y=1.14,
                    yanchor="top"
                ),
            ]
        )#---End Coding by Andrada Pancu