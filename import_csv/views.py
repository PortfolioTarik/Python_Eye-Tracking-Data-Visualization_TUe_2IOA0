from django.shortcuts import render

import csv
import io
from django.contrib import messages
from import_csv.models import FixationData
import pandas as pd

# full file written by Laura 1385739
# Create your views here.


def upload_csv(request):
    template = "website_import.html"
    data = FixationData.objects.all()

    prompt = {'profiles': data}

    if request.method == "GET":
        return render(request, template, prompt)

    csvfile = request.FILES['file']

    if not csvfile.name.endswith('.csv'):
        list(messages.get_messages(request))
        messages.add_message(request, messages.INFO, 'This is not a csv file')
        return render(request, template, prompt)

    if csvfile.name.endswith('csv'):
        list(messages.get_messages(request))
        messages.add_message(request, messages.INFO,
                             'csv file succesfully uploaded')

    df_eye = pd.read_csv(csvfile, encoding='unicode_escape', sep="\t")
    print(df_eye.info())

    rows = []
    for i in range(len(df_eye)):
        rows.append(
            FixationData(
                Timestamp=df_eye.iloc[i][0],
                StimuliName=df_eye.iloc[i][1],
                FixationIndex=df_eye.iloc[i][2],
                FixationDuration=df_eye.iloc[i][3],
                MappedFixationPointX=df_eye.iloc[i][4],
                MappedFixationPointY=df_eye.iloc[i][5],
                user=df_eye.iloc[i][6],
                description=df_eye.iloc[i][7],
            )
        )

    print(rows)
    # FixationData.objects.bulk_create(rows)

    # dataset = csvfile.read().decode('UTF-8', 'replace')

    # io_string = io.StringIO(dataset)
    # next(io_string)
    # for column in csv.reader(io_string, delimiter='\t'):
    #     _, created = FixationData.objects.update_or_create(
    #         timestamp = column[0],
    #         stimuli_name = column[1],
    #         fixation_index = column[2],
    #         fixation_duration = column[3],
    #         mapped_fixation_point_X = column[4],
    #         mapped_fixation_point_Y = column[5],
    #         user = column[6],
    #         description = column[7]
    #     )

    context = {}

    return render(request, template, context)
