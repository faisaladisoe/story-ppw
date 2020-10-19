from django.shortcuts import render, redirect
from .forms import CourseForm
from .models import Course

# Create your views here.
def index(request):
    content = {
        'socmed' : [
            {
                'link' : 'https://www.instagram.com/faisaladisoe/?hl=id',
                'alternate' : 'instagram'
            },
            {
                'link' : 'https://twitter.com/__patagonia_',
                'alternate' : 'twitter'
            },
            {
                'link' : 'https://github.com/faisaladisoe',
                'alternate' : 'github'
            },
            {
                'link' : 'mailto:faisaladi27@gmail.com',
                'alternate' : 'gmail'
            },
            {
                'link' : 'https://www.linkedin.com/in/m-faisal-adi-soesatyo-2b27611b6/',
                'alternate' : 'linkedin'
            }
        ]
    }

    return render(request, 'story1/index.html', content)

def copyright(request):
    content = {
        'copyright' : [
            {
                'title' : 'Freepik',
                'link' : 'https://www.flaticon.com/authors/freepik'
            },
            {
                'title' : 'Pixel Perfect',
                'link' : 'https://www.flaticon.com/authors/pixel-perfect'
            },
            {
                'title' : 'Flat Icons',
                'link' : 'https://www.flaticon.com/authors/flat-icons'
            },
            {
                'title' : 'Prosymbols',
                'link' : 'https://www.flaticon.com/authors/prosymbols'
            },
            {
                'title' : 'xnimrodx',
                'link' : 'https://www.flaticon.com/free-icon/school_3232526'
            },
            {
                'title' : 'Smashicons',
                'link' : 'https://www.flaticon.com/authors/smashicons'
            },
            {
                'title' : 'Gregor Cresnar',
                'link' : 'https://www.flaticon.com/authors/gregor-cresnar'
            },
            {
                'title' : 'iconixar',
                'link' : 'https://www.flaticon.com/authors/iconixar'
            },
            {
                'title' : 'Eucalyp',
                'link' : 'https://creativemarket.com/eucalyp'
            }
        ]
    }

    return render(request, 'story1/copyright.html', content)

def intro(request):
    return render(request, 'intro/intro.html')

def prototype(request):
    return render(request, 'story2/prototype.html')

def initialDesign(request):
    return render(request, 'story3/initDesign.html')

def copyrightInit(request):
    return render(request, 'story3/copyright-init.html')

def courseRegister(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courseList/')

    content = {
        'form' : form
    }

    return render(request, 'story5/courseRegister.html', content)

def courseList(request):
    data = Course.objects.all()
    content = {
        'data' : data
    }

    return render(request, 'story5/courseList.html', content)

def courseDetails(request, course_name):
    data = Course.objects.all().filter(course_name = course_name)
    content = {
        'data' : data
    }

    return render(request, 'story5/courseDetails.html', content)

def courseUpdate(request, pk):
    data = Course.objects.get(id = pk)
    form = CourseForm(instance = data)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance = data)
        if form.is_valid():
            form.save()
            return redirect('../../courseList/')

    content = {
        'form' : form
    }

    return render(request, 'story5/courseUpdate.html', content)

def courseDelete(request, pk):
    data = Course.objects.get(id = pk)
    if request.method == 'POST':
        data.delete()
        return redirect('../../courseList/')

    content = {
        'item' : data.course_name
    }
    return render(request, 'story5/courseDelete.html', content)

# def events(request):
#     data = Event.objects.all()
#     content = {
#         'data' : data
#     }
#     return render(request, 'story6/events.html', content)

# def eventDetails(request, pk):
#     data = Event.objects.all().filter(event = pk)
#     visitor = Visitor.objects.all().filter(event_id = data[0].id)
#     content = {
#         'data' : data,
#         'visitor' : visitor
#     }

#     return render(request, 'story6/eventDetails.html', content)

# def addEvents(request):
#     form = EventForm()
#     if request.method == 'POST':
#         form = EventForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('../')

#     content = {
#         'form' : form
#     }
#     return render(request, 'story6/addEvents.html', content)

# def deleteEvents(request, pk):
#     data = Event.objects.get(id = pk)
#     if request.method == 'POST':
#         data.delete()
#         return redirect('../../')

#     content = {
#         'item' : data.event
#     }
#     return render(request, 'story6/deleteEvents.html', content)

# def registerVisitor(request, pk):
#     form = VisitorForm()
#     data = Event.objects.get(id = pk)
#     if request.method == 'POST':
#         form = VisitorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('../../eventDetails/{}/'.format(data))

#     content = {
#         'form' : form,
#         'data' : data,
#     }
#     return render(request, 'story6/registerVisitor.html', content)