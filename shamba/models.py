
from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models as gismodels
# Create your models here.

class Incidences(models.Model):
    name = models.CharField(max_length=50)
    location= gismodels.PointField(srid=4326)
    objects = gismodels.Manager()


    def __unicode__ (self):
          return self.name

    
    class Meta:
        verbose_name_plural = "Incidences"

  


