# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('doc/', views.docIndex, name='doc'),
    path('', views.index, name='home'),
    path('blank', views.project, name='blank'),
    path('track', views.project, name='track'),
    path('tracking', views.project, name='tracking'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
