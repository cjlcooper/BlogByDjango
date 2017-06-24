# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime

def index(request):
	context = {}
	context['hello'] = 'Hello Django'
	return render(request, 'index.html', context)

	