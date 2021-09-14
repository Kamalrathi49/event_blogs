from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

reaction = (
    ("True", "LIKE"),
    ("False", "UNLIKE"),
)

class Event(models.Model):
    event_name = models.CharField(max_length=199)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    location = models.CharField(max_length=199) 
    image = models.ImageField(blank=True, null=True, upload_to="images/")
    is_liked = models.CharField(max_length=6, choices=reaction, null=True, blank=True, default='False')
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creater')

    def __str__(self):
        return self.event_name