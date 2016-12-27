from django.shortcuts import render
from django.conf import settings
from .forms import KittenForm
from .models import Kitten_image
from datetime import datetime
import requests


def kitten_home(request):
    if request.method == 'POST':
        form = KittenForm(request.POST)
        print "milsmils"

        if form.is_valid():
            print "mils"
            obj = Kitten_image()
            title = str(datetime.now())
            url = "http://placekitten.com/g/" + form.cleaned_data['input_width'] + "/" + form.cleaned_data['input_height']
            kitten = requests.get(url)
            f = open( title + ".png", "w")
            f.write(kitten.content)
            f.close
            obj.image_name = title + ".png"
            obj.width = form.cleaned_data['input_width']
            obj.height = form.cleaned_data['input_height']
            obj.save()

    else:
        form = KittenForm()

    all_image = Kitten_image.objects.all()

    x = ""
    for index in range(len(all_image)):
        if index % 4 == 0:
            x += '<div class="row">'+'<div class="col-xs-6 col-sm-3"><img src="' + settings.STATIC_URL + all_image[index].image_name + '"></div>'
        elif index % 4 == 3:
            x += '<div class="col-xs-6 col-sm-3"><img src="' + settings.STATIC_URL + all_image[index].image_name + '"></div>'+ '</div>'
        else:
            x += '<div class="col-xs-6 col-sm-3"><img src="' + settings.STATIC_URL + all_image[index].image_name + '"></div>'
    x += '</div>'


    print form.errors
    return render(request, 'kitten_home.html', {'kitten_image': all_image, 'n' : x})
