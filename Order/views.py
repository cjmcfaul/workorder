from django.shortcuts import render, redirect

from Order.models import WorkOrder, Task
from Order.forms import WorkOrderForm, TaskForm



# Create your views here.
def create_wo(request):
    form_class = WorkOrderForm

    if request.method == 'POST':

        form = form_class(request.POST)

        if form.is_valid():
            workorder = form.save(commit=False)

            workorder.save()

            return redirect('workorder', workorder_id=workorder.id)

    else:

        form = form_class()

    return render(request, 'work_order/create_wo.html', {
        'form' : form,
    })

def edit_wo(request, workorder_id):

    workorder = WorkOrder.objects.get(pk=workorder_id)
    unit = workorder.unit
    address = workorder.unit.address
    try:
        tasks = Task.objects.all().filter(case=workorder)
    except:
        tasks = None

    form_class = TaskForm

    if request.method == 'POST':

        form = form_class(request.POST)

        if form.is_valid():
            task = form.save(commit=False)

            task.case = workorder

            task.save()

            return redirect('workorder', workorder_id=workorder.id)

    else:

        form = form_class()

    return render(request, 'work_order/edit_wo.html',{
        'workorder' : workorder,
        'unit' : unit,
        'address' : address,
        'tasks' : tasks,
        'form' : form,
    })


def workorder(request, workorder_id):
    workorder = WorkOrder.objects.get(pk=workorder_id)
    unit = workorder.unit
    address = workorder.unit.address
    try:
        tasks = Task.objects.all().filter(case=workorder)
    except:
        tasks = None
    return render(request, 'work_order/wo.html',{
        'workorder' : workorder,
        'unit' : unit,
        'address' : address,
        'tasks' : tasks,
    })

def index(request):
    workorders = WorkOrder.objects.all()
    tasks = Task.objects.all()
    return render(request,'index.html', {
        'workorders' : workorders,
        'tasks' : tasks,
    })
