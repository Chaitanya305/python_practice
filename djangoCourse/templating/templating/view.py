from django.http import HttpResponse
from django.shortcuts import render

def get(request):
    param = {"name":"Chaitanya", "place":"Nashik"}    # to pass param
    return render(request, 'index.html', param)