from django import forms
class Studentform(forms.Form):
    firstname = forms.CharField(label="enter the first name", max_length=50)
    lastname = forms.CharField(label="enter the lastname", max_length=50)
    email = forms.EmailField(label="enter the email")
    file = forms.FileField() #for creating file inputs