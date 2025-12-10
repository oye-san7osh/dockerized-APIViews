from django.db import models
from django.utils import timezone
from decimal import Decimal


# Create your models here.

# Employee Model
class EmployeeModel(models.Model):
    
    class StatusChoices(models.TextChoices):
        
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"
        ON_LEAVE = "on_leave", "On Leave"
    
    full_name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10,unique=True)
    employee_id = models.CharField(max_length=10, unique=True)
    
    position = models.CharField(max_length=25)
    department = models.CharField(max_length=25)
    
    
    # Foreign key to Branch (must create branch model separately)
    branch = models.ForeignKey(
        "BranchModel",
        on_delete=models.SET_NULL,
        null=True,
        related_name="employees"
    )
    
    
    # Self-referencing for manager
    manager = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="team_members"
    )
    
    
    join_date = models.DateField(default=timezone.now)
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.ACTIVE
    )
    
    def __str__(self):
        return f"{self.full_name} ({self.employee_id})"


# Branch Model
class BranchModel(models.Model):
    
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=100, blank=True)
    
    
    # Branch manager (points to employee)
    manager = models.ForeignKey(
        "EmployeeModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_branches"
    )
    
    
    # This is not stored in DB - calculated automatically
    
    @property
    def number_of_employees(self):
        return self.employees.count() # related_name="employees" in Employee model
    
    
    def __str__(self):
        return self.name
    
 
    
 # Salary Model
class SalaryModel(models.Model):
        
    employee = models.ForeignKey(
        "EmployeeModel",
        on_delete=models.CASCADE,
        related_name="salaries"
    )
    
    base_salary = models.DecimalField(max_digits=12, decimal_places=2)
    bonus = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    allowances = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    
    salary_month = models.DateField(default=timezone.now)
    
    net_salary = models.DecimalField(max_digits=12, decimal_places=2, editable=False)
    
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now=True)
    
    
    # Automatically calculate net salary
    def save(self, *args, **kwargs):
        
        self.net_salary = self.base_salary + self.bonus + self.allowances - self.deductions
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return f"{self.employee.full_name} - {self.salary_month.strftime('%B %Y')}"
        


    
    
    
    