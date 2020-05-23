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
def getUserData(user, mapName):
    columns = ['ID', 'Timestamp', 'StimuliName', 'FixationIndex', 'FixationDuration',
               'MappedFixationPointX', 'MappedFixationPointY', 'user', 'description']
    columns_sql = ', '.join(columns)
    queryset_userData = FixationData.objects.raw(
        "SELECT " + columns_sql + " FROM Fixation_data WHERE user = '" + user + "' AND StimuliName LIKE '%" + mapName + "' ")
    return querySetToPandas(queryset_userData)