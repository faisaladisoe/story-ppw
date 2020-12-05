from django.shortcuts import render
from django.http import JsonResponse
import json, requests

# Create your views here.
def bookCollection(request):
    return render (request, 'bookCollection.html')

def jsonResult(request):
    query = request.GET.get('q', 'Trump') # default value of the dictionary is Trump
    params = "https://www.googleapis.com/books/v1/volumes?q=" + query
    data = requests.get(params).json()
    return JsonResponse(data, safe=False)
