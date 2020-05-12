from django.db import models
import os
from django.conf import settings


def stimuli_path():
    return os.path.join(settings.BASE_DIR, 'stimuli/')


class FixationData(models.Model):
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

    def __str__(self):
        return self.StimuliName
        # return self.Timestamp + ' ' + self.MappedFixationPointX + ' ' + self.MappedFixationPointY
