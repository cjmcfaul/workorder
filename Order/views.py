from django.shortcuts import render, redirect

from Order.models import WorkOrder
from Order.forms import WorkOrderForm



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


def workorder(request, workorder_id):
    workorder = WorkOrder.objects.get(pk=workorder_id)
    unit = workorder.unit
    address = workorder.unit.address
    return render(request, 'work_order/wo.html',{
        'workorder' : workorder,
        'unit' : unit,
        'address' : address,
    })

def index(request):
    workorders = WorkOrder.objects.all()
    return render(request,'index.html', {
        'workorders' : workorders,
    })
