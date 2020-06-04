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
    return userData

#Get all the data of the user for a particular map.
def getUserData(user, mapName, color):
    columns = ['ID', 'Timestamp', 'StimuliName', 'FixationIndex', 'FixationDuration',
               'MappedFixationPointX', 'MappedFixationPointY', 'user', 'description']
    columns_sql = ', '.join(columns)
    query = "SELECT " + columns_sql + " FROM Fixation_data WHERE user = '" + user + "' AND StimuliName LIKE '%" + mapName.split('_')[1] + "%' AND description = '" + color + "'"
    print('query sent:' + query)
    queryset_userData = FixationData.objects.raw(query)
    return querySetToPandas(queryset_userData)

def getAllStimulis():
    query_maps = FixationData.objects.raw("SELECT DISTINCT StimuliName, 1 as id FROM Fixation_data ")
    stimuli_list = []
    for stimulidata in query_maps: 
        stimuli_list.append(str(stimulidata.StimuliName))
    return stimuli_list

def getAllUsersByStimuli(stimuli):
    query_users = FixationData.objects.raw("SELECT DISTINCT user, 1 as id FROM Fixation_data WHERE StimuliName LIKE '%" + stimuli.split('_')[1] + "%' ORDER BY CAST(substr(user, 2, length(user)) as integer) ASC;")
    user_list = []
    for userEach in query_users: 
        user_list.append(userEach.user)
    return user_list

#Start of code by Andrada Pancu
def getSortedUserData(user, mapName, color, order):
    columns = ['ID', 'Timestamp', 'StimuliName', 'FixationIndex', 'FixationDuration',
               'MappedFixationPointX', 'MappedFixationPointY', 'user', 'description']
    columns_sql = ', '.join(columns)

    query_asc = "SELECT " + columns_sql + " FROM Fixation_data WHERE user = '" + user + "' AND StimuliName LIKE '%" + mapName.split('_')[1] + "%' AND description = '" + color + "' ORDER BY FixationDuration "
    query_desc = "SELECT " + columns_sql + " FROM Fixation_data WHERE user = '" + user + "' AND StimuliName LIKE '%" + mapName.split('_')[1] + "%' AND description = '" + color + "' ORDER BY FixationDuration DESC "

    if order == 'ASC' :
        queryset_userData = FixationData.objects.raw(query_asc)
    if order == 'DESC' :
        queryset_userData = FixationData.objects.raw(query_desc)
    
    return querySetToPandas(queryset_userData)
#End of code by Andrada Pancu