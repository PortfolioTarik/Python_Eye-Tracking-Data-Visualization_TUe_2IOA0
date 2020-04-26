from django.shortcuts import render

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import pandas as pd


def home(request):
    df_eye = pd.read_csv(
        'C:/Users/TARIKSSD/Desktop/2IOA0 - Project/2ioa0-23a-eye-tracking-and-visualization/import_csv/csv/all_fixation_data_cleaned_up.csv', encoding='unicode_escape', sep="\t")
    #source = ColumnDataSource(df_eye)
    title = 'y = f(x)'

    plot = figure(title=title,
                  x_axis_label='X-Axis',
                  y_axis_label='Y-Axis',
                  plot_width=400,
                  plot_height=400)

    plot.line(df_eye['Timestamp'], df_eye['MappedFixationPointX'],
              legend_label='f(x)', line_width=2)
    # Store components
    script, div = components(plot)

    # Feed them to the Django template.
    return render(request, 'website_import.html',
                  {'script': script, 'div': div})
