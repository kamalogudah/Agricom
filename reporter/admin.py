# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
from .models import Incidences, Sublocations
#from leaflet.admin import

class IncidencesAdmin(LeafletGeoAdmin):
    list_display = ('name','location')

class SublocationsAdmin(LeafletGeoAdmin):
    list_display = ('subloc','area')

admin.site.register(Incidences, IncidencesAdmin) 
admin.site.register(Sublocations, SublocationsAdmin)
