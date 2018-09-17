from django.http import HttpResponse
from django.shortcuts import render


def welcome(request):
    return HttpResponse("Hello, world!")

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print (request.user)
    #return HttpResponse("HOME: Hello, world!")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    print(args, kwargs)
    print (request.user)
    #return HttpResponse("HOME: Hello, world!")
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    print(args, kwargs)
    print (request.user)
    my_context = {
        "my_text": "This is about us",
        "is_this_true": True,
        "my_number": 123,
        "my_list": [123, 42434, 5678, "ABC"],
    }
    #return HttpResponse("HOME: Hello, world!")
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    print(args, kwargs)
    print (request.user)
    #return HttpResponse("HOME: Hello, world!")
    return render(request, "social.html", {})


















