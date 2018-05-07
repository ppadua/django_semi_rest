from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^', include('apps.semi_restful.urls')), 
	url(r'^users/', include('apps.semi_restful.urls')), 
]	
