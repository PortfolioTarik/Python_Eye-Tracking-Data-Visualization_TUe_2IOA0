#coded by Andrada Pancu

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

#---- Start Coding by Tarik Hacialiogullari
#fig.show()
# create stimuli list > create traces for each stimuli > set to trigger 1 by 1 via dropdown
# with query input
columns = ['ID', 'Timestamp', 'StimuliName', 'FixationIndex', 'FixationDuration',
               'MappedFixationPointX', 'MappedFixationPointY', 'user', 'description']

    columns_sql = ', '.join(columns)
    query_maps = FixationData.objects.raw(
        "SELECT DISTINCT StimuliName, 1 as id FROM Fixation_data ")

    stimuli_list = ["StimuliName:"]

    for stimulidata in query_maps: 
        stimuli_list.append(stimulidata.StimuliName)

#---- End Coding by Tarik Hacialiogullari
for i in len(stimuli_list):
    if i != "StimuliName:":
        fig.add_trace(
            go.Scatter( x = ''' SELECT MappedFixationPointX FROM Fixation_data WHERE 'StimuliName' = i ''',
                y=''' SELECT MappedFixationPointY FROM Fixation_data WHERE 'StimuliName' = i ''',
                name = stimuli_list[i],
                if i>1: visible=False ))
                
    

# Dropdown with traces, enabling them via 'visible' for their respective buttons
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

# dropdowns for user comparison page

# color dropdown
fig.update_layout(
        updatemenus=[
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
                    dict(
                        args=["colorscale", "Viridis"],
                        label="Viridis",
                        method="restyle"
                    ),
                    dict(
                        args=["colorscale", "Cividis"],
                        label="Cividis",
                        method="restyle"
                    ),
                ]),
                # position might need updating when you move it
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.12,
                xanchor="left",
                y=1.10,
                yanchor="top"
            ),
        ]
)

