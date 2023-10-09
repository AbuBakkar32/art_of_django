from django.http import HttpResponse


def index(request, name):
    a = f"<h1>Hello World! Im {name}</h1>"
    return HttpResponse(a)


def about(request):
    return HttpResponse("<h1>About Page</h1>")


def contact(request):
    return HttpResponse("<h1>Contact Page</h1>")
