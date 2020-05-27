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
    query_maps = FixationData.objects.raw(
        "SELECT DISTINCT StimuliName, 1 as id FROM Fixation_data ")

    stimuli_list = ["StimuliName:"]

    for stimulidata in query_maps: 
        stimuli_list.append(stimulidata.StimuliName)


for i in len(stimuli_list):
    if i != "StimuliName:":
        fig.add_trace(
            go.Scatter( x = ''' SELECT MappedFixationPointX FROM Fixation_data WHERE 'StimuliName' = i ''',
                y=''' SELECT MappedFixationPointY FROM Fixation_data WHERE 'StimuliName' = i ''',
                name = stimuli_list[i],
                if i>1: visible=False ))
                
    


fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args={"visible": [True, False, False, False, False, False, False]},
                    label=stimuli_list[1],
                    method="update"
                ),
                dict(
                    args={"visible": [False, True, False, False, False, False, False]},
                    label=stimuli_list[2],
                    method="update"
                ),
                dict(
                    args={"visible": [False, False, True, False, False, False, False]},
                    label=stimuli_list[3],
                    method="update"
                ),
                dict(
                    args={"visible": [False, False, False, True, False, False, False]},
                    label=stimuli_list[4],
                    method="update"
                ),
                dict(
                    args=["type", "surface"],
                    label=stimuli_list[5],
                    method="update"
                ),
                dict(
                    args=["type", "surface"],
                    label=stimuli_list[6],
                    method="update"
                ),
                dict(
                    args=["type", "surface"],
                    label=stimuli_list[7],
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