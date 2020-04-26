from bokeh.plotting import figure, output_file, show
import numpy as np
import pandas as pd


df = pd.read_csv('all_fixation_data_cleaned_up.csv', delimiter="\t", engine="python")
#df = pd.read_csv('C:/Users/Egresits fanni/Documents/TUe Eindhoven/2IOA0 - HTI Webtech/all_fixation_data_cleaned_up.csv')
print(df.head())

# prepare some data
x = df[df['StimuliName'] =='01_Antwerpen_S1.jpg']["MappedFixationPointX"]
y = df[df['StimuliName'] =='01_Antwerpen_S1.jpg']["MappedFixationPointY"]

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple scatter example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.scatter(x, y, legend_label="Temp.", line_width=2)

# show the results
show(p)