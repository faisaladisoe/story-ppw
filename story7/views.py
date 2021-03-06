from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'login')
def accordion(request):
    content = {
        'data': [
            {
                'title': 'My Activity',
                'topic': 'Learning new stuff, Pursue my ambition, Shape my dream'
            },
            {
                'title': 'Experience',
                'topic': 'I have no experience both in organisation and comittee'
            },
            {
                'title': 'Achievement',
                'topic': 'I have no achievement at all'
            },
            {
                'title': 'Dream',
                'topic': 'I want to be a CEO and an investor'
            }
        ]
    }
    return render(request, 'story7/accordion.html', content)
    