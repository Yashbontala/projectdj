from django.urls import path 
from .views import home_view, result_view
  
urlpatterns = [ 
    path('frequency', home_view ,name="urlsearch"),
    path('result',result_view,name="urlresult"), 
] 