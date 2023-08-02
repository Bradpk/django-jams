from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=200)

class Artist(models.Model):
    name = models.CharField(max_length=200)

class Album(models.Model):
    name = models.CharField(max_length=200)

class Genre(models.Model):
    type = models.CharField(max_length=200)

class User(models.Model):
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)