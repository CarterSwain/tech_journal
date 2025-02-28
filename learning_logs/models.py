from django.db import models

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200) # max_length is required for CharField.
    date_added = models.DateTimeField(auto_now_add=True) # auto_now_add=True sets the current date and time when a user creates a new topic.
    
    def __str__(self):
       return self.text  # This makes Django admin display the actual topic name.
    
class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # on_delete=models.CASCADE deletes all entries associated with the topic when the topic is deleted.
    text = models.TextField() # TextField does not require a size limit
    date_added = models.DateTimeField(auto_now_add=True) # auto_now_add=True sets the current date and time when a user creates a new entry.
    
    class Meta:
        verbose_name_plural = 'entries' # Meta holds extra information for managing a model; verbose_name_plural is a human-readable name for a group of entries.

    def __str__(self):
        """Return a simple string representing the entry."""
        return f"{self.text[:50]}..." # Return the first 50 characters of the text attribute, followed by an ellipsis, if the entry is longer than 50 characters.
