from django.shortcuts import render

# Coded by Laura except when noted.
from django.contrib import messages
from import_csv.models import FixationData
import pandas as pd

def upload_csv(request):
    template = "website_import.html"
    #data = FixationData.objects.all()

    prompt = {'profiles': 'data'}

    csvfile = 0
    if request.method == "GET":
        return render(request, template, prompt)
        csvfile = request.FILES['file']

    # save the uploaded file as csvfile
    
    if csvfile == 0:
        list(messages.get_messages(request))
        messages.add_message(request, messages.INFO, 'select a file')
        return render(request, template, prompt)

    # check whether the file is of the correct type
    if csvfile != 0 and not csvfile.name.endswith('.csv'):
        list(messages.get_messages(request))
        messages.add_message(request, messages.INFO, 'This is not a csv file')
        return render(request, template, prompt)

    # Give an update to the website user that a file has been uploaded
    if csvfile.name.endswith('csv'):
        list(messages.get_messages(request))
        messages.add_message(request, messages.INFO,
                             'csv file succesfully uploaded')

    #---Start Coding by Tarik Hacialiogullari
    df_eye = pd.read_csv(csvfile, encoding='unicode_escape', sep='\t')
    print(df_eye)

    #fill the dataset using the uploaded file
    #rows = []
    #for i in range(len(df_eye)):
    #    print(df_eye[i])
        #rows.append(
        #    FixationData(
        #        Timestamp=df_eye.iloc[i][0],
        #        StimuliName=df_eye.iloc[i][1],
        #        FixationIndex=df_eye.iloc[i][2],
        #        FixationDuration=df_eye.iloc[i][3],
        #        MappedFixationPointX=df_eye.iloc[i][4],
        #        MappedFixationPointY=df_eye.iloc[i][5],
        #        user=df_eye.iloc[i][6],
        #        description=df_eye.iloc[i][7],
        #    )
        #)
        #if ((i % 10000) == 0):
        #    print(str(i))

    # print(rows)
    #FixationData.objects.bulk_create(rows)
    #---End Coding by Tarik Hacialiogullari

    

# The initial coding by Laura to upload a dataset, updated due to loadingtime issues
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
