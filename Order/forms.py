from django import forms
from django.forms import ModelForm

from Order.models import WorkOrder, Task, Subtask
from Property.models import Room

class WorkOrderForm(ModelForm):
    class Meta:
        model=WorkOrder
        fields = (
            'name',
            'unit',
            'staff',
        )

class SubtaskForm(ModelForm):
    class Meta:
        model=Subtask
        fields = (
            'name',
            'complete',
        )

class TaskForm(ModelForm):

    #room_select = forms.ModelMultipleChoiceField(queryset=None)
    #item_select = forms.ModelMultipleChoiceField(queryset=None)

    class Meta:
        model=Task
        fields = (
            'name',
            'stage',
            'room',
            'item',
            'task_type',
            'date_created',
            'date_assigned',
            'date_scheduled',
            'date_completed',
            'vendor',
            'description',
        )

    #def __init__(self, *args, **kwargs):

    #    super(TaskForm, self).__init__(*args, **kwargs)

    #    self.fields['room_select'].queryset = Room.objects.filter(room_unit=room.unit)
