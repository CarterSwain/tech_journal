from django.shortcuts import render

from .models import Topic

def index(request):
    """The home page for Tech Journal."""
    return render(request, 'tech_journal/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'tech_journal/topics.html', context)

def topic(request, topic_id): # topic_id is a parameter that matches the value captured by the regex in the URL pattern.
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id) # Retrieve the topic with the id captured by the URL pattern.
    entries = topic.entry_set.order_by('-date_added') 
    context = {'topic': topic, 'entries': entries} # Pass the topic and its associated entries to the template.
    return render(request, 'tech_journal/topic.html', context)
