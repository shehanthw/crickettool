from unittest.util import _MAX_LENGTH
from django.db import models

class AllPlayer(models.Model):
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    team1 = models.CharField(max_length=200)
    team2 = models.CharField(max_length=200)
    team3 = models.CharField(max_length=200)
    team4 = models.CharField(max_length=200)
    team5 = models.CharField(max_length=200)
    team6 = models.CharField(max_length=200)
    team7 = models.CharField(max_length=200)
    team8 = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team1