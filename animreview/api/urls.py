from xml.etree.ElementInclude import include

from django.urls import path, include


urlpatterns = [
    path('v1/', include('v1.urls'))
]
