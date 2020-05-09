#Create slider steps and traces
for step in np.arange(0, 5, 0.1):
    fig.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color="#03b6fc", width=6)#,
            # name="𝜈 = " + str(step),
            # x=np.arange(0, 10, 0.01),
            # y=np.sin(step * np.arange(0, 10, 0.01)))) - for testing with no data

# Make last trace visible
fig.data[10].visible = True

# Create Slider
steps = []
for i in range(0,1600):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "Slider switched to step: " + str(i)}],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "What_parameter_slider_changes: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)


#dash slider
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()
app.layout = html.Div(
      html.Div([
            html.Div([html.H5("Level"),

                    dcc.Slider(id='slider_input',
                                min=0,
                                max=1,
                                step=0.005,
                                value=0.1,
                    )],style={'width': '200'}
                ),

            html.Div(style={'height': '10'}),

            html.Div(dcc.Input( id='text_input',
                        placeholder='Enter a value...',
                        type='text',
                        value=0.0
                    ),style={'width': '50'}),

            dcc.Graph(id='example',
                     figure={'data':[{'x':[1,2],
                                      'y':[0,1],
                                      'type':'bar',
                                      'marker':dict(color='#ffbf00')
                                     }],
                              'layout': go.Layout(title='Plot',
                                                  #xaxis = list(range = c(2, 5)),
                                                  yaxis=dict(range=[0, 1])
                                                   )
                               })

          ], style={'width':'500', 'height':'200','display':'inline-block'})
)

# callback - 1 (from slider)
@app.callback(Output('example', 'figure'),
             [Input('slider_input', 'value'),
             Input('text_input', 'value')])

def update_plot(slider_input, text_input):
    if (float(text_input)==0.0):
        q = float(slider_input)
    else:
        q = float(text_input)



#slider version 3 - no dash
import json
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot 
init_notebook_mode(connected=True)

init_notebook_mode(connected=True)
cf.go_offline()

#create traces
traces = []
q = np.linspace(0,1, 100)
for i in range(0,len(q)):
    trace = dict(
                type = 'bar',
                visible = False,
                x=[1, 2],
                y=[q[i], 1 - q[i]],
                marker=dict(color='#ffbf00'),
                width=0.5
             )
    traces.append(trace)

traces[0]['visible'] = 'True'

#create slider
steps=[]
for i in range(len(traces)):
    step = dict(
        method = 'restyle',  
        args = ['visible', [False] * len(traces)],
        label=""
    )
    step['args'][1][i] = True # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active = 10,
    currentvalue = {"prefix": "Level: "},
    #pad = {"t": 50},
    steps = steps

)]

#layout
layout = go.Layout(
    width=500,
    height=500,
    autosize=False,
    yaxis=dict(range=[0, 1])
)

layout['sliders'] = sliders