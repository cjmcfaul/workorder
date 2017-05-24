from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class WorkOrder(models.Model):
    name = models.CharField(max_length=200)
    staff = models.ManyToManyField('Person.Staff')
    unit = models.ForeignKey(
        'Property.Unit',
        null = True,
    )

    def __str__(self):
        return '{}'.format(self.name)

class Task(models.Model):

    TYPE = (
        ("D","Drywall"),
        ("E","Electrical"),
        ("P","Painting"),
        ("PG","Plumbing"),
        ("PL","Plaster"),
        ("R","Replacement"),
        ("A","Appliance"),
        ('T', "Trash Removal"),
        ('O', 'Other'),
    )

    STAGE = (
        ("C","Created"),
        ("G","Getting Quote"),
        ("A","Assigned Vendor"),
        ("S","Scheduled"),
        ("N","Needs Reviews"),
        ("D","Done"),
    )

    name = models.CharField(
        max_length=200,
        null = True,
        blank = True,
        )

    case = models.ForeignKey(
        'Order.WorkOrder',
        null = True,
        blank = True,
        )

    room = models.ManyToManyField(
        'Property.Room',
        blank= True,
        )

    item = models.ManyToManyField(
        'Property.Item',
        blank= True,
        )

    vendor = models.ForeignKey(
        'Person.Vendor',
        blank = True,
        null = True,
        )

    task_type = models.CharField(
        max_length = 1,
        choices = TYPE,
        null=True
        )

    stage = models.CharField(
        max_length = 1,
        choices = STAGE,
        default = "C",
        )

    date_created = models.DateTimeField(
        default=timezone.now)

    date_assigned = models.DateTimeField(
        blank = True,
        null = True,
        )

    date_scheduled = models.DateTimeField(
        blank = True,
        null = True,
    )

    date_completed = models.DateTimeField(
        blank = True,
        null = True,
    )

    description = models.TextField(null=True)

    sub_task= models.ManyToManyField(
        'Order.Subtask',
        blank = True,
    )

    review = models.ManyToManyField(
        'Order.Review',
        blank = True
        )

    def __str__(self):
        return '{}'.format(self.name)

class Subtask(models.Model):

    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    date_completed = models.DateTimeField(
        blank = True,
        null = True,
    )
    complete = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.name)

class Review(models.Model):

    date_time = models.DateTimeField(default=timezone.now,null=True)
    description = models.TextField(null=True)
