from django import forms
from .models import Product
from geo.models import Region, District
class ProductForm(forms.ModelForm):
    region = forms.ModelChoiceField(queryset=Region.objects.all())
    city = forms.ModelChoiceField(queryset=District.objects.all())
    class Meta:
        model = Product
        exclude = ['slug']
        
