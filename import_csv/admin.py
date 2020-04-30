from django.contrib import admin

# Register your models here.
from .models import FixationData

class FixationDataAdmin(admin.ModelAdmin):
    list_display = (
        'timestamp', 
        'stimuli_name', 
        'fixation_index', 
        'fixation_duration', 
        'mapped_fixation_point_X',
        'mapped_fixation_point_Y',
        'user',
        'description'
    )

admin.site.register(FixationData, FixationDataAdmin)