from django.contrib import admin

# Register your models here.
from Property.models import Room, Unit, Address, Item

admin.site.register(Address)
admin.site.register(Unit)
admin.site.register(Room)
admin.site.register(Item)
