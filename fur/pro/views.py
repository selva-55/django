from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
import json
from .models import products_details

# Create your views here.
@api_view(['GET'])
def sel(request):
    if request.method == 'GET':
        sd = products_details.objects.all()
        return HttpResponse(sd,content_type='application/json')