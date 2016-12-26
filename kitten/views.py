from django.shortcuts import render
from .forms import KittenForm
import requests


def kitten_home(request):
    if request.method == 'POST':
        form = KittenForm(request.POST)
        print "milsmils"

        if form.is_valid():
            print "mils"
            url = "http://placekitten.com/g/" + form.cleaned_data['input_width'] + "/" + form.cleaned_data['input_height']
            kitten = requests.get(url)
            f = open("kittens.png", "w")
            f.write(kitten.content)
            f.close
    else:
        form = KittenForm()

    print form.errors
    return render(request, 'kitten_home.html', {'kitten_image': "kittens.png"})
