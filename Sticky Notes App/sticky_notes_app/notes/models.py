from django.db import models


# Create your models here.
class Note(models.Model):
    """ Models representing a Sticky Note model

    Fields:
    - title: CharField for the Note title with a max length of 255 characters
    - Content: TextField for the Note content
    - created_at:  DateTimeField set to the current date and time when the
        post is created.

    Methods:
    - __str__: Returns a string representation of the Note, showing the title
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
