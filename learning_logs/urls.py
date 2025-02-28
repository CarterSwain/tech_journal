""" Defines URL patterns for tech_journal. """

from django.urls import path

from .import views

app_name = 'tech_journal'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
]