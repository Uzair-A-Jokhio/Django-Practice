from django.contrib import admin
from myapp.models import Person
from myapp.models import Employee
# Register your models here.


admin.site.register(Person)
admin.site.register(Employee)