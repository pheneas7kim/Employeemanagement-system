# employees/models.py
from django.db import models

class Employee(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('both', 'Both'),
    ]

    employee_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name
