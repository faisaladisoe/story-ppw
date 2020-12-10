import json, requests
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'login')
def bookCollection(request):
    return render (request, 'bookCollection.html')

@login_required(login_url = 'login')
def jsonResult(request):
    query = request.GET.get('q', 'Trump') # default value of the dictionary is Trump
    params = "https://www.googleapis.com/books/v1/volumes?q=" + query
    data = requests.get(params).json()
    return JsonResponse(data, safe=False)
