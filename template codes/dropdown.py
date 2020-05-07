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