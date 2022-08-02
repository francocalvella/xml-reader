from Xml.views import xml 
from django.urls import path

urlpatterns = [
    path('', xml, name='xml')
]