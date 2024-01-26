from django.db import models

# Create your models here.

class Person(models.Model):
    person_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    gen = (("Male","Male"),("Female","Female"))
    gender = models.CharField(max_length=20, choices=gen, default=1)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.person_name
    
class Employee(models.Model):
    employee_name = models.ForeignKey(Person, on_delete=models.PROTECT, default=None )
    employee_id = models.IntegerField()
    salary = models.IntegerField()