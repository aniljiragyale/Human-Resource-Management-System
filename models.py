from django.db import models


CATEGORY_CHOICES = (
    ('HR', 'Human resources'),
    ('F', 'Financial'),
    ('M_P', 'Manufacturing and production'),
    ('S_M', 'Sales and marketing'),
    ('IT', 'Technology')
)

ATTENDENCE = (
    ('A', 'ABSENT'),
    ('P', 'PRESENT')
)


class Employee(models.Model):
    """Model representing an employee."""

    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    department = models.CharField(choices=CATEGORY_CHOICES, max_length=5)
    joining_date = models.DateField()
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=300)


def __str__(self):
    """String representation of an employee."""
    return self.name


class Attendence(models.Model):
    """Model representing attendance records for employees."""

    date = models.DateField()
    department = models.CharField(choices=CATEGORY_CHOICES, max_length=5)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendence = models.CharField(choices=ATTENDENCE, max_length=2)
    time_in = models.TimeField(default='00:00:00')
    time_out = models.TimeField(default='00:00:00')

def __str__(self):
    """String representation of an attendance record."""
    return f"{self.employee.name} - {self.date} - {self.get_attendance_display()}"

