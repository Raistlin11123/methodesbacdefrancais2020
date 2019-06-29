from . import views
from django.urls import path

urlpatterns = [
    #Maybe a generic view?
    path('corpus', views.corpus_view, name='corpus'),
    path('commentaire', views.commentaire_view, name='commentaire'),
    path('contact', views.contact_view, name='contact'),
]