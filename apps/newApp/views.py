from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    if not 'user_id' in request.session:
        return redirect('/')
    return render(request, 'newApp/index.html')
