from django.http import HttpResponse


def index(request, name):
    a = f"<h1>Hello World! Im {name}</h1>"
    return HttpResponse(a)
