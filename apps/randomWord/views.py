# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    context = {
        'word': get_random_string(4)
    }
    if not 'word' in request.session:
        request.session['word'] = "-"
    if not 'count' in request.session:
        request.session['count'] = 0
    
    return render(request,'randomWord/index.html', context)

def generate(request):
    request.session['count'] += 1
    return redirect('/')
    
def refresh(request):
    request.session['count'] = 0
    return redirect('/')


