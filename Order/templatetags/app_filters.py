from django import template

register = template.Library()

@register.filter(name='get_vendor_work_orders')
def get_vendor_work_orders(tasks):

    workorders = []

    for task in tasks:

        if workorders.__contains__(task.case):

            return

        else:
            workorders.append(task.case)

    return workorders
