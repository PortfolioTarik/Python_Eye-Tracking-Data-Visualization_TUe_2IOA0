# Generated and coded by Tarik Hacialiogullari except when noted.
from django.shortcuts import render
import csv
import io
from django.contrib import messages
from import_csv.models import FixationData
import pandas as pd



def upload_csv(request):
    template = "website_import.html"
    data = ''
    #---Start Coding by Laura van der Bij
    prompt = {'profiles': data}

    if request.method == "GET":
        return render(request, template, prompt)
    #---End Coding by Laura van der Bij

    #check if there is a file selected given.
    if bool(request.FILES.get('filepath', False)) == True:
        csvfile = request.FILES['file']
    else:
        return render(request, template, prompt)

    #---Start Coding by Laura van der Bij
    # check whether the file is of the correct type
    if not csvfile.name.endswith('.csv'):
        list(messages.get_messages(request))
        messages.add_message(request, messages.INFO, 'This is not a csv file')
        return render(request, template, prompt)

    # Give an update to the website user that a file has been uploaded
    if csvfile.name.endswith('csv'):
        list(messages.get_messages(request))
        messages.add_message(request, messages.INFO,
                             'csv file succesfully uploaded')
    #---End Coding by Laura van der Bij

    #Read with Pandas the CSV by tab delimited.
    df_eye = pd.read_csv(csvfile, encoding='unicode_escape', sep="\t")
    print(df_eye.info())
    #Delete all previous data.
    FixationData.objects.raw("DELETE FROM Fixation_data ")
    #fill the dataset using the uploaded file
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
        if ((i % 10000) == 0):
            print(str(i))

    FixationData.objects.bulk_create(rows)
    context = {}

    return render(request, template, context)
