from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
	#url(r'^$', views.post_list, name='post_list')
    #path('admin/', admin.site.urls),
    path('', views.index)
]
