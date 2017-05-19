from django import forms
from django.forms import ModelForm

from Order.models import WorkOrder, Task

class WorkOrderForm(ModelForm):
    class Meta:
        model=WorkOrder
        fields = (
            'name',
            'unit',
            'staff',
        )

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields = (
            'name',
            'room',
            'item',
            'task_type',
            'vendor',
            'description',
        )
