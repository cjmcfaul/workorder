from django.contrib import admin

from Person.models import Vendor, Staff, Owner, Tenant
# Register your models here.


admin.site.register(Vendor)
admin.site.register(Staff)
admin.site.register(Owner)
admin.site.register(Tenant)
