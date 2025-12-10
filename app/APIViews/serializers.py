from rest_framework import serializers
from APIViews.models import EmployeeModel, BranchModel, SalaryModel


class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = EmployeeModel
        fields = ['id', 'full_name', 'email', 'contact', 'employee_id', 'position', 'department', 'branch', 'manager', 'join_date', 'status', ]
    


class BranchSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = BranchModel
        fields = ['id', 'name', 'address', 'contact_details', 'manager', ]



class SalarySerializer(serializers.ModelSerializer):
    
    net_salary = serializers.DecimalField(
            max_digits=12,
            decimal_places=2,
            read_only=True
        )
    
    class Meta:
        
        model =SalaryModel
        fields = ['id', 'employee', 'base_salary', 'bonus', 'allowances', 'deductions', 'salary_month', 'net_salary', 'created_at', 'updated_at', ]
        
    
    def validate(self, attrs):
        
        base = attrs.get("base_salary")
        bonus = attrs.get("bonus")
        
        
        # Only validate if BOTH are provided (handle PATCH safely)
        if base is not None and bonus is not None:
            if bonus > base:
                raise serializers.ValidationError(
                    "Bonus Cannot be higher than base salary."
                    )
        return attrs
        