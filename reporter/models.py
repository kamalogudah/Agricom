# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Incidences"

class Sublocations(models.Model):
    area = models.FloatField()
    perimeter = models.FloatField()
    kensl89g_field = models.FloatField()
    kensl89g_i = models.FloatField()
    subloc = models.CharField(max_length=254)
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.subloc