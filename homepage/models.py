#Tarik Hacialiogullari
from django.db import models
from import_csv.models import FixationData
import numpy as np
import pandas as pd

#Tool convert Django QuerySet to Pandas Dataframe
def querySetToPandas(queryset_userData):
    dtypes = np.dtype([
        ('Timestamp', int),
        ('StimuliName', str),
        ('FixationIndex', int),
        ('FixationDuration', int),
        ('MappedFixationPointX', int),
        ('MappedFixationPointY', int),
        ('user', str),
        ('description', str)
        ])
    data = np.empty(0, dtype=dtypes)
    userData = pd.DataFrame(data)

    for fixatData in queryset_userData: 
        dics = dict(
                        Timestamp = fixatData.Timestamp, 
                        StimuliName = str(fixatData.StimuliName), 
                        FixationIndex = fixatData.FixationIndex, 
                        FixationDuration = fixatData.FixationDuration, 
                        MappedFixationPointX = fixatData.MappedFixationPointX, 
                        MappedFixationPointY = fixatData.MappedFixationPointY, 
                        user = str(fixatData.user), 
                        description = str(fixatData.description)
                    )
        userData = userData.append(dics, ignore_index=True)
    return userData.drop_duplicates(subset=None, keep='first', inplace=False)

#Get all the data of the user for a particular map.
def getUserData(user, mapName, color):
    trimmed_stimuli = mapName[mapName.find("_"):]
    columns = ['ID', 'Timestamp', 'StimuliName', 'FixationIndex', 'FixationDuration',
               'MappedFixationPointX', 'MappedFixationPointY', 'user', 'description']
    columns_sql = ', '.join(columns)
    query = "SELECT " + columns_sql + " FROM Fixation_data WHERE user = '" + user + "' AND StimuliName LIKE '%" + trimmed_stimuli + "%' AND description = '" + color + "'"
    # print('query sent:' + query)
    queryset_userData = FixationData.objects.raw(query)
    return querySetToPandas(queryset_userData)

def getAllStimulis():
    query_maps = FixationData.objects.raw("SELECT DISTINCT StimuliName, 1 as id FROM Fixation_data ")
    stimuli_list = []
    for stimulidata in query_maps: 
        stimuli_list.append(str(stimulidata.StimuliName))
    return stimuli_list

def getAllUsersByStimuliAndColor(stimuli, color):
    #start = stimuli.find('_') + 1
    trimmed_stimuli = stimuli[stimuli.find("_"):]
    query_raw = "SELECT DISTINCT user, 1 as id FROM Fixation_data WHERE StimuliName LIKE '%" + trimmed_stimuli + "%' AND description = '" + color + "'  ORDER BY CAST(substr(user, 2, length(user)) as integer) ASC;"
    # print("--------------------------")
    # print(query_raw)
    # print("--------------------------")
    query_users = FixationData.objects.raw(query_raw)
    user_list = []
    for userEach in query_users: 
        user_list.append(userEach.user)
    return user_list

# def deleteAll():
#     FixationData.objects.raw("DELETE FROM Fixation_data ")
#     return stimuli_list

# def checkExistingData():
#         columns = ['ID', 'Timestamp', 'StimuliName', 'FixationIndex', 'FixationDuration',
#                'MappedFixationPointX', 'MappedFixationPointY', 'user', 'description']
#     columns_sql = ', '.join(columns)
#     query_maps = FixationData.objects.raw("(SELECT TOP 1 user FROM Fixation_data) (SELECT TOP 1 user FROM Fixation_data) ")
#     return 
#     stimuli_list = []
#     for stimulidata in query_maps: 
#         stimuli_list.append(str(stimulidata.StimuliName))
#     return stimuli_list

def getPreUserByColor(color):
    preUser = FixationData.objects.raw("SELECT user, StimuliName, 1 as id FROM Fixation_data WHERE description = '"+color+"' ORDER BY id ASC LIMIT 1")
    mapName = ''
    userName = ''
    for pre in preUser:
        mapName = pre.StimuliName
        userName = pre.user
    return getUserData(userName, mapName, color)

def getPreUserByColorAndStimuli(color, stimuli):
    trimmed_stimuli = stimuli[stimuli.find("_"):]
    preUser = FixationData.objects.raw("SELECT user, StimuliName, 1 as id FROM Fixation_data WHERE description = '"+color+"' AND StimuliName LIKE '%" + trimmed_stimuli + "%' ORDER BY id ASC LIMIT 1")
    mapName = ''
    userName = ''
    for pre in preUser:
        mapName = pre.StimuliName
        userName = pre.user
    return getUserData(userName, mapName, color)