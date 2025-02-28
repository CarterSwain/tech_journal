from django.shortcuts import render

def index(request):
    """The home page for Tech Journal."""
    return render(request, 'tech_journal/index.html')
