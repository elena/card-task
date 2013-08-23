# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Project
# Location

"""
There are 2 simple purpose:
* Capture every thought, idea, todo, "gotta remember", task
* Post-capture management to break down in to bite-sized, practical, doable tasks.

Most basic unit is a "card". Every thing get chucked in as a card.

Some of these things can come and go, but some (perhaps most) need/should to be
broken down into realistic tasks.

The idea is to be like a linked-list or daisy-chain of tasks.

Children cards, morphed in to something else.

"Project" and "Location".

Bug tracking systems are great, simplified but more flexible version.

Single "Mission" going at any given time.
"""

class Card(models.Model):
    user = models.ForeignKey(User)
    todo = models.CharField(max_length=2048)
    active = models.BooleanField(default=True)
    time_added = models.DateTimeField(auto_now_add=True)
    time_complete = models.DateTimeField(auto_now_add=True)


# class Project(models.Model):
#     pass


# class Location(models.Model):
#     pass


# class CardDue(models.Model):
#     time_due = models.DateTimeField(null=True, blank=True)


# class Recur(models.Model):
#     todo = models.ForeignKey(Card)
#     freq = models.PositiveIntegerField(help_text="In seconds")


# class Mission(models.Model):
#     mission = models.CharField(max_length=254)


# class MissionCard(models.Model):
#     mission = models.ForeignKey(Mission)
#     card = models.ForeignKey(Card)
#     time_added = models.DateTimeField(auto_now_add=True)
