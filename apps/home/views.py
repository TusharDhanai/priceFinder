# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.conf import settings
from django.db.models import Q
from apps.home.models import Product
import os
import json
import pandas as pd

def index(request):
    suggestions = Product.objects.filter(category__exact='mobile')[:10]
    
    template = loader.get_template('project/index.html')
    context= {
        "suggestions": list(suggestions)
    }
    return HttpResponse(template.render(context,request))

def docIndex(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

def project(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.

    load_template = request.path.split('/')[-1]
    context['segment'] = load_template

    html_template = loader.get_template('project/' + load_template + '.html')
    return HttpResponse(html_template.render(context, request))

def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def search(request):
    request_data = request.POST


    if (request_data['query'] != ''):
        all_objects = Product.objects.values().filter(
            Q(name__contains=request_data['query']) | Q(category__contains=request_data['query']))[:20]

        context = {
            "query": request_data.dict(),
            "products": list(all_objects)
        }
    else:
        context = {
            "query": '',
            "products":None
        }

    html_template = loader.get_template('project/search.html')
    return HttpResponse(html_template.render(context,request))

def insertProduct(request):
    product = pd.read_csv(os.path.join(settings.FLIPKART_DIR,"categories/mobile/mobile.csv"))
    html_template = product.to_json(orient="records")

    data = json.loads(html_template)

    product = Product()
    product.insert(data,'mobile')

    return HttpResponse(data)