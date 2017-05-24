from django.shortcuts import render, redirect

from django.utils import timezone

from Person.models import Vendor
from Order.models import WorkOrder, Task, Subtask
from Order.forms import WorkOrderForm, TaskForm, SubtaskForm

from backend import get_vendor_work_orders

#Vendor Views

def vendor_detail(request, vendor_id):
    vendor = Vendor.objects.get(pk=vendor_id)
    workorders = WorkOrder.objects.all()
    tasks = Task.objects.all().filter(vendor=vendor)
    return render(request, 'vendor/vendor_detail.html',{
        'tasks' : tasks,
        'vendor' : vendor,
        'workorders' : workorders,
    })


#Task Views

def create_task(request, workorder_id):

    workorder = WorkOrder.objects.get(pk=workorder_id)
    unit = workorder.unit
    address = workorder.unit.address
    #rooms = unit.objects.all().filter()
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

    return render(request, 'task/create_task.html',{
        'workorder' : workorder,
        'unit' : unit,
        'address' : address,
        'tasks' : tasks,
        'form' : form,
    })

def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    current_stage = task.stage
    form_class = TaskForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=task)
        if form.is_valid():

            form.save()

            if current_stage != task.stage:
                if task.stage == 'A' and task.date_assigned == None:
                    task.date_assigned = timezone.now()

                elif task.stage == 'S' and task.date_scheduled == None:
                    task.date_scheduled = timezone.now()

                elif task.stage == 'D' and task.date_scheduled == None:
                    task.date_completed = timezone.now()

                form.save()


                return redirect('task_detail', task_id=task.id)


            else:

                form.save()

                return redirect('task_detail', task_id=task.id)


    else:
        form = form_class(instance=task)

    return render(request, 'task/edit_task.html', {
        'task' : task,
        'form' : form,
    })

def task_detail(request,task_id):
    task = Task.objects.get(pk=task_id)
    workorder = task.case
    form_class = SubtaskForm

    if request.method == 'POST':

        form = form_class(request.POST)

        if form.is_valid():
            subtask = form.save(commit=False)

            subtask.save()

            #task.sub_task = form

            #task.save()

            return redirect('task_detail', task_id=task.id)

    else:

        form = form_class()
    return render(request, 'task/task_detail.html',{
        'task' : task,
        'workorder' : workorder,
        'form' : form,
    })

# Work Order Views
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

    form_class = WorkOrderForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=workorder)
        if form.is_valid():
            form.save()
            return redirect('workorder', workorder_id=workorder.id)
    else:
        form = form_class(instance=workorder)

    return render(request, 'work_order/edit_wo.html', {
        'workorder': workorder,
        'form': form,
    })

def vendor_wo(request, vendor_id, workorder_id):
    workorder = WorkOrder.objects.get(pk=workorder_id)
    unit = workorder.unit
    address = workorder.unit.address
    vendor = Vendor(pk=vendor_id)
    tasks = Task.objects.all().filter(case=workorder_id)
    complete_tasks = tasks.filter(stage='D')
    return render(request, 'work_order/vendor_wo.html',{
        'workorder' : workorder,
        'unit' : unit,
        'address' : address,
        'tasks' : tasks,
        'vendor' : vendor,
        'complete_tasks' : complete_tasks,
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
