from django import forms
from .models import Order


class contactform(forms.ModelForm):
    class Meta:
        models = Order
        fields = [' ']
