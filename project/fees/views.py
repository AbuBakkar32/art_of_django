from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render


def index(request):
    return render(request, 'fees/index.html')
