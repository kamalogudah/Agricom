from django.conf.urls import include,url
from views import HomePageView, sublocation_datasets

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name = 'home'),
     url(r'^sublocations_data/$', sublocation_datasets, name = 'subloc'),
      url(r'^incidence_data/$', HomePageView.as_view(), name = 'home'),
   
]