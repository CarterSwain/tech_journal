from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm, EntryForm

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

def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tech_journal:topics') # Redirect the user to the topics page.
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'tech_journal/new_topic.html', context)

def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('tech_journal:topic', topic_id=topic_id)
    
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'tech_journal/new_entry.html', context)
