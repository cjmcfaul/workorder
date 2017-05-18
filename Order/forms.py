from django import forms
from django.forms import ModelForm

from Order.models import WorkOrder

class WorkOrderForm(ModelForm):
    class Meta:
        model=WorkOrder
        fields = (
            'name',
            'unit',
            'staff',
        )
