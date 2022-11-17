# from asyncio.windows_events import INFINITE
from datetime import datetime
from django.db import models



    
class Artiste(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    age = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.first_name  
    
    
class Song(models.Model):
    title = models.CharField(max_length = 40)
    rel_date = models.DateField(default = datetime.today)
    likes = models.IntegerField(default = 0)
    artiste_id = models.ForeignKey(Artiste, null= True, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
 
    
class Lyric(models.Model):     
    content = models.TextField(default = '')
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.content
# Create your models here.
