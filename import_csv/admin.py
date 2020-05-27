from django.contrib import admin

# Register your models here.
from .models import FixationData


class FixationDataAdmin(admin.ModelAdmin):
    list_display = (
        'Timestamp',
        'StimuliName',
        'FixationIndex',
        'FixationDuration',
        'MappedFixationPointX',
        'MappedFixationPointY',
        'user',
        'description'
    )


admin.site.register(FixationData, FixationDataAdmin)
