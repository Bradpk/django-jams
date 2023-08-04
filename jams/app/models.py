from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ManyToManyField('Artist')
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    genre = models.ManyToManyField('Genre')
    # user = models.ManyToManyField('User')

    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Genre(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type

class User(models.Model):
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    #playlist = models.ForeignKey('Playlist', on_delete=models.CASCADE)

    def __str__(self):
        return self.username
    
class Playlist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name