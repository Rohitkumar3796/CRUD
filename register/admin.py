from django.contrib import admin
from register.models import *

# Register your models here.

@admin.register(Employee)
class emplAdmin(admin.ModelAdmin):
    list_display=['empId','empname','empemail','emppass','empmobile','empaddress']