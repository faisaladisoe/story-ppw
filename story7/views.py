from django.shortcuts import render

# Create your views here.
def accordion(request):
    return render(request, 'story7/accordion.html')