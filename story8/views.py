from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .forms import BookForm
import requests

# Create your views here.
def bookCollection(request):
    data = ''
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            query = request.POST['bookName']
            params = 'https://www.googleapis.com/books/v1/volumes?q=' + query
            data = requests.get(params).json()
    content = {
        'form' : form,
        'data' : data
    };
    return render(request, 'bookCollection.html', content)

