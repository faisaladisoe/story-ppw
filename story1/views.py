from .models import Course
from .forms import CourseForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'login')
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

@login_required(login_url = 'login')
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

@login_required(login_url = 'login')
def intro(request):
    return render(request, 'intro/intro.html')

@login_required(login_url = 'login')
def prototype(request):
    return render(request, 'story2/prototype.html')

@login_required(login_url = 'login')
def initialDesign(request):
    return render(request, 'story3/initDesign.html')

@login_required(login_url = 'login')
def copyrightInit(request):
    return render(request, 'story3/copyright-init.html')

@login_required(login_url = 'login')
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

@login_required(login_url = 'login')
def courseList(request):
    data = Course.objects.all()
    content = {
        'data' : data
    }

    return render(request, 'story5/courseList.html', content)

@login_required(login_url = 'login')
def courseDetails(request, course_name):
    data = Course.objects.all().filter(course_name = course_name)
    content = {
        'data' : data
    }

    return render(request, 'story5/courseDetails.html', content)

@login_required(login_url = 'login')
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

@login_required(login_url = 'login')
def courseDelete(request, pk):
    data = Course.objects.get(id = pk)
    if request.method == 'POST':
        data.delete()
        return redirect('../../courseList/')

    content = {
        'item' : data.course_name
    }
    return render(request, 'story5/courseDelete.html', content)
    