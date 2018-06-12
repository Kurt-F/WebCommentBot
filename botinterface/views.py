from django.shortcuts import render
from django.shortcuts import HttpResponse
from .messagehandling import *
# Create your views here.


def test_view(request):
    return HttpResponse("test")