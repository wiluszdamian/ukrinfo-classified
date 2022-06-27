from django.shortcuts import render

posts = [
    {
        'author': 'Damian Wilusz',
        'title': 'Ogloszenie nr1',
        'content': 'Jakis tam opis',
        'date_posted': 'June 26, 2022'
    },
    {
        'author': 'Diana Blazejowska',
        'title': 'Ogloszenie nr2',
        'content': 'Jakis opis tam',
        'date_posted': 'June 27, 2022'
    },

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home/homepage.html', context)
