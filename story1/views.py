from django.shortcuts import render

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
            }
        ]
    }

    return render(request, 'story1/copyright.html', content)