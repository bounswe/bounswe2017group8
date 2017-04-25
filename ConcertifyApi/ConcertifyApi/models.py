# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Registered users
class User(models.Model):
	name = models.CharField(max_length=50, blank=True, default='')
	username = models.CharField(max_length=24, blank=True, default='defaultuser')
	location = models.CharField(max_length=24, blank=True, default='')
	favorite_musician = models.CharField(max_length=36, blank=True, default='')

	class Meta:
                ordering = ('username',)
                
# Musician information
class Musician(models.Model):
	name = models.CharField(max_length=36, blank=True, default='')
	genre = models.CharField(max_length=24, blank=True, default='')
	tag = models.CharField(max_length=24, blank=True, default='')

	class Meta:
		ordering = ('name',)

# Location information
class Location(models.Model):
	name = models.CharField(max_length=36, blank=True, default='')
	address = models.CharField(max_length=24, blank=True, default='')
	latitude = models.FloatField(default=0)
	longtitude = models.FloatField(default=0)

	class Meta:
		ordering = ('name',)

# Tag information
class Tag(models.Model):
	ID = models.IntegerField(default=0)
	text = models.CharField(max_length=20, blank=True, default='')

	class Meta:
		ordering = ('ID',)


# Concert information
class Concert(models.Model):
        name = models.CharField(max_length=50, blank=True, default='')
        location = models.CharField(max_length=24, blank=True, default='')
        musician = models.CharField(max_length=24, blank=True, default='')

        class Meta:
                ordering = ('name',)
