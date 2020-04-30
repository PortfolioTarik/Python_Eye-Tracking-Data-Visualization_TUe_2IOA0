from django.db import models
import os
from django.conf import settings

def stimuli_path():
    return os.path.join(settings.BASE_DIR, 'stimuli/')

class FixationData(models.Model):
    timestamp = models.IntegerField()
    stimuli_name = models.FilePathField(path=stimuli_path)
    fixation_index = models.IntegerField()
    fixation_duration = models.IntegerField()
    mapped_fixation_point_X = models.IntegerField()
    mapped_fixation_point_Y = models.IntegerField()
    user = models.CharField(max_length=5)
    description = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'Fixation_data'

    def __str__(self):
        return self.stimuli_name