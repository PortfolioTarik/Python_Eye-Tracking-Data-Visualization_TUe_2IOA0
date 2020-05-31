# Coded by Laura updated by Tarik Hacialiogullari
from django.db import models
import os
from django.conf import settings


def stimuli_path():
    return os.path.join(settings.BASE_DIR, 'stimuli/')

# Creation of class of the data, with the specification for each column content
class FixationData(models.Model):
    list_display = ('Timestamp', 'StimuliName', 'FixationIndex', 'FixationDuration',
                    'MappedFixationPointX', 'MappedFixationPointY', 'user', 'desription')
    Timestamp = models.IntegerField()
    StimuliName = models.FilePathField(path=stimuli_path)
    FixationIndex = models.IntegerField()
    FixationDuration = models.IntegerField()
    MappedFixationPointX = models.IntegerField()
    MappedFixationPointY = models.IntegerField()
    user = models.CharField(max_length=5)
    description = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'Fixation_data'

# functions for retrieving specific data information
    def __str__(self):
        # return self.StimuliName
        return str(self.Timestamp) + ', ' + str(self.MappedFixationPointX) + ', ' + str(self.MappedFixationPointY)

    def get_Timestamp(self):
        return self.Timestamp

    def get_FixationDuration(self):
        return self.FixationDuration
