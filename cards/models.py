from django.db import models
from django.contrib.auth.models import User


# Mission
# Project

class Card(models.Model):
    user = models.ForeignKey(User)
    todo = models.CharField(max_length=254)
    time_added = models.DateTimeField(auto_now_add=True)
    time_due = models.DateTimeField(null=True, blank=True)


class Recur(models.Model):
   todo = models.ForeignKey(Card)
   freq = models.PositiveIntegerField(help_text="In seconds")
