from django.conf.urls import url
from django.contrib import admin
from . import views as calc

urlpatterns = [
    url(r'^index/', calc.index, name="index"),
    url(r"^add/(?P<a>\d+)/(?P<b>\d+)", calc.add),
    url(r"^divide/(?P<a>\d+)/(?P<b>\d+)", calc.division),
    url(r"^substract/(?P<a>\d+)/(?P<b>\d+)", calc.substract),
    url(r"^multiply/(?P<a>\d+)/(?P<b>\d+)", calc.multiply)
]
