from django.contrib import admin

# Register your models here.
from Order.models import Task, Review, WorkOrder

admin.site.register(Task)
admin.site.register(Review)
admin.site.register(WorkOrder)
