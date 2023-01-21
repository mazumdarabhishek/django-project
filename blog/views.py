from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
posts = [
    {
        'author': 'Abhishek',
        'title': 'Dummy Blog 1',
        'content': 'This is a dummy blog',
        'date_posted': 'January 21, 2023'
    },
    {
        'author': 'Mazumdar',
        'title': 'Dummy Blog 2',
        'content': 'This is a dummy blog',
        'date_posted': 'January 22, 2023'
    }
]


def home(request):
    context = {
        'posts': posts
        
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html")