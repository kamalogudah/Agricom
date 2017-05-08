import os
from django.contrib.gis.utils import LayerMapping
from .models import Sublocations
# Auto-generated `LayerMapping` dictionary for Sublocations model
sublocations_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'kensl89g_field' : 'KENSL89G_',
    'kensl89g_i' : 'KENSL89G_I',
    'subloc' : 'SUBLOC',
    'geom' : 'MULTIPOLYGON',
}

sublocation_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/kenya_sublocations.shp'))
def run(verbose=True):
    lm = LayerMapping(Sublocations, sublocation_shp, sublocations_mapping, transform = False,encoding = 'iso-8859-1')
    lm.save(strict=True, verbose=verbose)