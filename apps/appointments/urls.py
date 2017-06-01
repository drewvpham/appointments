from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_appointment$', views.add_appointment),
    url(r'^success$', views.success),
]
