""" Defines URL patterns for tech_journal. """

from django.urls import path

from .import views

app_name = 'learning_logs' # This line allows Django to distinguish this urls.py file from other urls.py files in the project.
urlpatterns = [
    # Home page.
    path('', views.index, name='index'), # The name 'index' allows us to refer to this URL pattern when building links in templates.
    # Show all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Path for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]