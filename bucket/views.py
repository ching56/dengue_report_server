from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == 'GET':
        res = HttpResponse("hi bucket")
    # elif request.method == 'POST':
        # do_something_else()
    return res