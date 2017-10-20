# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


from bs4 import BeautifulSoup
import selenium.webdriver as webdriver

# Create your views here.

@csrf_exempt
def getInstaPic(request, userName):
    """
    List all the the pics of the userName
    """
    if request.method == "GET":
        rate = []
        _url = 'https://www.instagram.com/'+userName
        #_url = 'https://www.instagram.com/arpit_tiwari_312'
        driver = webdriver.Firefox()
        driver.get(_url)
        className = '_4rbun'
        soup = BeautifulSoup(driver.page_source)
        #print(soup)
        for story_heading in soup.find_all(class_= className):
            rate.append((story_heading.img['src']))
        
        #print(rate)
        return JsonResponse(rate, safe=False)
    
    