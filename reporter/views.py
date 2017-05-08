# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from models import Sublocations, Incidences 

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

def sublocation_datasets(request):
    sublocations = serialize('geojson', Sublocations.objects.all())
    return HttpResponse(sublocations, content_type ='json')

def incidence_datasets(request):
    incidences = serialize('geojson', Incidences.objects.all())
    return HttpResponse(incidences, content_type= 'json')
