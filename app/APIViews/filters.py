import django_filters
from django.db import models
from datetime import date, timedelta
from APIViews.models import EmployeeModel, BranchModel, SalaryModel
from django.db.models import Q

class EmployeeFilter(django_filters.FilterSet):
    
    
    # 1 Employee Model Filers

        # 1.1 Basic Information
        # A. by full name
    
    emp_name = django_filters.CharFilter(method="name_filter")
    
    def name_filter(self, queryset, name, value):
        
        return queryset.filter(
            Q(full_name__iexact=value) | 
            Q(full_name__icontains=value)
        )
    
    
    emp_contact = django_filters.CharFilter(method="contact_filter")
    
    def contact_filter(self, queryset, name, value):
        
        return queryset.filter(
            Q(email__icontains=value) |
            Q(contact__icontains=value)
        )
        
    emp_id = django_filters.CharFilter(field_name="employee_id", lookup_expr="iexact")
        
    class Meta:
        model = EmployeeModel
        fields = [
            "emp_name",
            "emp_contact",
            "emp_id",
            
        ]