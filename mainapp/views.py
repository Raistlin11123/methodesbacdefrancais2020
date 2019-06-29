#all the imports needed
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
import re #expressions régulières
#from .models import Profil, Clue, UserClues
from .forms import ContactForm
from django.core.mail import send_mail

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
            # send email code goes here
            send_mail(
                form.cleaned_data["name"],
                form.cleaned_data["content"],
                form.cleaned_data["email"],
                ['philippepavec@gmail.com'],
                fail_silently=False,
            )
            #here goes the success message and the redirecting
            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()
    return render(request, 'mainapp/contact.html', locals())