from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
class EmployeeProfile(models.Model):
    Employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='proflie')
    postion = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, black=true, null=True, blank=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    Date_of_birth = models.DateField(blank=True, null=True)
    Date_of_joining = models.DateField(blank=True, null=True)
    
    class intern(EmployeeProfile):
        class Meta:
            verbose_name = 'intern'
            verbose_name_plural = 'interns'
            
    class Manager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter()
            
            
            