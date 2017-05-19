from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Address(models.Model):
    line_one = models.CharField(max_length=300)
    line_two = models.CharField(
        max_length=300,
        blank = True,
        )
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)

    def __str__(self):
        return '{}'.format(self.line_one)

class Unit(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(
        'Property.Address',)

    def __str__(self):
        return '{}'.format(self.name)

class Room(models.Model):
    name = models.CharField(max_length=200)
    unit = models.ForeignKey(
        'Property.Unit',
        null = True,
        )

    def __str__(self):
        return '{}'.format(self.name)

class Item(models.Model):
    name = models.CharField(max_length=200)
    room_info = models.ForeignKey(
        'Property.Room',
        null = True,
    )

    def __str__(self):
        return '{}'.format(self.name)
