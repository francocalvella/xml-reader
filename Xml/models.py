from django.db import models

# Create your models here.

class AlbumXml(models.Model):
    title = models.CharField(max_length=40)
    release_year = models.DateField()
    author = models.CharField(max_length=40)
    best_song = models.CharField(max_length=40)
    xml = models.FileField(upload_to='media/albums')