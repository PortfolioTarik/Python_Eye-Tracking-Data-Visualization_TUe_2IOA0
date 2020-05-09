from bokeh.plotting import figure, output_file, show
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file



df = pd.read_csv('all_fixation_data_cleaned_up.csv', delimiter="\t", engine="python")
#df = pd.read_csv('C:/Users/Egresits fanni/Documents/TUe Eindhoven/2IOA0 - HTI Webtech/all_fixation_data_cleaned_up.csv')
#print(df.head())

#copy dataset with specialized columns (just for testing something)
test = df[['user', 'StimuliName']].copy()
#print(test[(test['StimuliName'] == '07_Moskau_S1.jpg') & (test['user'] == 'p1')])

#print(test[test['user'] == "p2"] & test[test['StimuliName'] == "07_Moskau_S1.jpg"])
# prepare some data 3 criteria
x = df[(test['StimuliName'] == '06_Hamburg_S1.jpg') & (test['user'] == 'p1')]["MappedFixationPointX"]
y = df[(test['StimuliName'] == '06_Hamburg_S1.jpg') & (test['user'] == 'p1')]["MappedFixationPointY"]
z = df[(test['StimuliName'] == '06b_Hamburg_S2.jpg') & (test['user'] == 'p16')]["MappedFixationPointX"]
w = df[(test['StimuliName'] == '06b_Hamburg_S2.jpg') & (test['user'] == 'p16')]["MappedFixationPointY"]
print(z)

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure( plot_width=800, plot_height=600, x_range=(0,1651), y_range=(0,1200),
            title="Gaze plot of Hamburg of the first user", x_axis_label='Mapped Fixation Point X',
            y_axis_label='Mapped Fixation Point Y')

# add a line renderer with legend and line thickness
p.line(x, y, legend_label="P1.", line_width=2, color = "red")
p.line(z, w, legend_label="P16.", line_width=2, color = "blue")
p.circle(x, y, fill_color="red",
color = "red", size = 8)

#add background
p.image_url(url=['06_Hamburg_S1.jpg'], x=0, y=1200, w=1651, h=1200, alpha=0.3)

# show the results
show(p)