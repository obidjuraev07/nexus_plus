from django import forms
class Send_email(forms.Form):
    name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class" : "form-control",
                                                                        'placeholder': "Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class" : "form-control",
                                                           'placeholder': "Email"}))
    Subject = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class" : "form-control",
                                                                           'placeholder': "Subject"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class" : "form-control",
                                                                           'placeholder': "Message"}))