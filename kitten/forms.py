from django import forms

class KittenForm(forms.Form):
    input_width = forms.CharField(label='input_width', max_length=10)
    input_height = forms.CharField(label='input_height', max_length=10)

