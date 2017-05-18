from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Vendor(models.Model):

    TYPE = (
        ("E","Exterminator"),
        ("P","Plumber"),
        ("Z","Electrician"),
        ("G","General Contractor"),
        ("H","Handy Man"),
    )

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    vendor_type = models.CharField(
        max_length=1,
        choices = TYPE,
        )

    def __str__(self):
        return '{}'.format(self.name)

class Tenant(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    unit = models.ForeignKey(
        'Property.Unit',
    )
    def __str__(self):
        return '{}'.format(self.name)

class Staff(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.name)

class Owner(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.name)
