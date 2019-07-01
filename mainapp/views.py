#all the imports needed
#python 
import re #expressions régulières

#django
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

#app
from .models import Contact
from .forms import ContactForm


#simple function which return the index page
def corpus_view(request):
    return render(request, 'mainapp/corpus.html', locals())

def commentaire_view(request):
    return render(request, 'mainapp/commentaire.html', locals())

#login required?
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # recup des infos
            name = form.cleaned_data["name"]
            content = form.cleaned_data["content"]
            email = form.cleaned_data["email"]
            
            #creation d'une nouvelle ligne pour le model de contact
            new_mail = Contact(name=name, email=email, content=content)
            new_mail.save()
            messages.success(request, 'Votre message a bien été envoyé')
            return redirect('contact')

            #here goes the success message and the redirecting
            
    else:
        form = ContactForm()
    return render(request, 'mainapp/contact.html', locals())