from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.views import ObtainJSONWebToken
from django.contrib.auth.models import User
from django.http import HttpResponse


def index(request, name):
    a = f"<h1>Hello World! Im {name}</h1>"
    return HttpResponse(a)




