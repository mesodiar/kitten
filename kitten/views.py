from django.shortcuts import render

def kitten_home(request):
    return render(request, 'kitten_home.html', {})
