from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="", max_length=30, widget= forms.TextInput(attrs={'placeholder':'Nom', 'class': "form-control"}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder':'Email', 'class': "form-control"}))
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder':'Ecrivez votre message ici ...', 'class': "form-control", }))