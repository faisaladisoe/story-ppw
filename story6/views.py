from django.shortcuts import render, redirect
from .forms import EventForm, VisitorForm
from .models import Event, Visitor

# Create your views here.
def events(request):
    data = Event.objects.all()
    content = {
        'data' : data
    }
    return render(request, 'story6/events.html', content)

def eventDetails(request, pk):
    data = Event.objects.all().filter(event = pk)
    if data.exists():
        visitor = Visitor.objects.all().filter(event_id = data[0].id)
        content = {
            'data' : data,
            'visitor' : visitor
        }
    else:
        content = {
            'data' : data
        }

    return render(request, 'story6/eventDetails.html', content)

def addEvents(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')

    content = {
        'form' : form
    }
    return render(request, 'story6/addEvents.html', content)

def deleteEvents(request, pk):
    data = Event.objects.get(id = pk)
    if request.method == 'POST':
        data.delete()
        return redirect('../../')

    content = {
        'item' : data.event
    }
    return render(request, 'story6/deleteEvents.html', content)

def registerVisitor(request, pk):
    form = VisitorForm()
    data = Event.objects.get(id = pk)
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../../eventDetails/{}/'.format(data))
    else:
        form = VisitorForm()

    content = {
        'form' : form,
        'data' : data,
    }
    return render(request, 'story6/registerVisitor.html', content)

def deleteVisitor(request, pk):
    data = Visitor.objects.get(id = pk)
    if request.method == 'POST':
        data.delete()
        return redirect('../../')

    content = {
        'item' : data.visitor_name
    }
    return render(request, 'story6/deleteVisitor.html', content)

def updateVisitor(request, pk):
    data = Visitor.objects.get(id = pk)
    form = VisitorForm(instance = data)
    if request.method == 'POST':
        form = VisitorForm(request.POST, instance = data)
        if form.is_valid():
            form.save()
            return redirect('../../')

    content = {
        'form' : form
    }
    return render(request, 'story6/updateVisitor.html', content)