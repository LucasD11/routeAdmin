#!/usr/bin/env python3
# coding=utf-8
# 
# Date: 2017-12-21 12:05:09
# 
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
]
