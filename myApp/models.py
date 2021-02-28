from django.db import models
from django.utils import timezone

# Create your models here.
class Song(models.Model):
    ID = models.IntegerField(unique=True)
    Name_of_the_song = models.CharField(max_length=100)
    Duration_in_sec = models.IntegerField()
    uploaded_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Name_of_the_song

class Podcast(models.Model):
    ID = models.IntegerField(unique=True)
    Name_of_the_Podcast= models.CharField(max_length=100)
    Duration_in_sec = models.IntegerField()
    uploaded_time = models.DateTimeField(default=timezone.now)
    Host = models.CharField(max_length=100)
    Participants = models.CharField(default=None,max_length=100)

    def __str__(self):
        return self.Name_of_the_Podcast
    
class Audiobook(models.Model):
    ID = models.IntegerField(unique=True)
    Title_of_the_audiobook= models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Narrator = models.CharField(max_length=100)
    Duration_in_sec = models.IntegerField()
    uploaded_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Title_of_the_audiobook