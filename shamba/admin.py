from django.contrib import admin
from  .models import Incidences
# from django.contrib.gis.db import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
    pass
    # list_display = ('name','location')




admin.site.register(Incidences,IncidencesAdmin)