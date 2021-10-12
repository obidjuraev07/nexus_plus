from django import forms
from .models import Blog,Comments


class BlogModelForm(forms.ModelForm):
    name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class" : "form-control",
                                                                        'placeholder': "Name"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class" : "form-control",
                                                                           'placeholder': "Description"}))

    class Meta:
        model = Blog
        fields = ['name', 'description', 'image', 'category']


    def save(self, commit=True):
        self.instance.created_date
        super().save()
        return self.instance


class Comment(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control","id":"comment-message"}))
