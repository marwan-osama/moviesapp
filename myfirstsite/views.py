from django.shortcuts import render
from movies.views import index


def home(request):
    return index(request)
