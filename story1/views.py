from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'story1/index.html')

def copyright(request):
    return render(request, 'story1/copyright.html')