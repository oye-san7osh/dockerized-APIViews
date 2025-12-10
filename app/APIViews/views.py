from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from APIViews.models import EmployeeModel, BranchModel, SalaryModel
from APIViews.serializers import EmployeeSerializer, BranchSerializer, SalarySerializer
from APIViews.paginations import ApiPagination
from APIViews.filters import EmployeeFilter


# For the Employees
class EmployeeListCreateView(APIView):
    permission_classes = [AllowAny]
    
    
    def get(self, request):
        
        employees = EmployeeModel.objects.all().order_by('-id')
        
        filtered_emp = EmployeeFilter(request.GET, queryset=employees).qs
        
        paginator = ApiPagination()
        result_page_emp = paginator.paginate_queryset(filtered_emp, request, view=self)
        
        serializer = EmployeeSerializer(result_page_emp, many = True)
        return paginator.get_paginated_response(serializer.data)
    
    
    def post(self, request):
        
        serializer = EmployeeSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class EmployeeDetailUpdateDelete(APIView):
    permission_classes = [AllowAny]
    
    def get_object(self, pk):
        try:
            employee = EmployeeModel.objects.get(pk = pk)
            return employee
        except EmployeeModel.DoesNotExist:
            return None
    
    def get(self, request, pk):
        
        employee = self.get_object(pk)
        
        if employee is None:
            return Response({"detail": "Employee not found"}, status=404)

        
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    
    def patch(self, request, pk):
        
        employee = self.get_object(pk)
        
        if employee is None:
            return Response({"detail": "Employee not found"}, status=404)

        
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request, pk):
        
        employee = self.get_object(pk)
        
        if employee is None:
            return Response({"detail": "Employee not found"}, status=404)

        
        serializer = EmployeeSerializer(employee, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        
        employee = self.get_object(pk)
        
        if employee is None:
            return Response({"detail": "Employee not found"}, status=404)

        
        employee.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    

class BranchListCreateView(APIView):
    permission_classes = [AllowAny]
    
    
    def get(self, request):
        
        branches = BranchModel.objects.all().order_by('-id')
        
        paginator = ApiPagination()
        result_page_branch = paginator.paginate_queryset(branches, request, view=self)
        
        serializer = BranchSerializer(result_page_branch, many = True)
        
        return paginator.get_paginated_response(serializer.data)
    
    
    def post(self, request):
        
        serializer = BranchSerializer(data = request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class BranchDetailUpdateDelete(APIView):
    permission_classes = [AllowAny]
    
    def get_object(self, pk):
         
        try:
            branch = BranchModel.objects.get(pk=pk)
            return branch
        except BranchModel.DoesNotExist:
            return None
    
    
    def get(self, request, pk):
        
        branch = self.get_object(pk)
        
        if branch is None:
            return Response({"detail": "Branch not found"}, status=404)

        
        serializer = BranchSerializer(branch)
        return Response(serializer.data)
    
    
    
    def put(self, request, pk):
        
        branch = self.get_object(pk)
        
        if branch is None:
            return Response({"detail": "Branch not found"}, status=404)

        
        
        serializer = BranchSerializer(branch, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        
        branch = self.get_object(pk)
        
        if branch is None:
            return Response({"detail": "Branch not found"}, status=404)

        
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


class SalaryListCreateView(APIView):
    permission_classes = [AllowAny]
    
    
    def get(self, request):
        
        salary = SalaryModel.objects.all().order_by('-id')
        
        paginator = ApiPagination()
        
        result_page_salary = paginator.paginate_queryset(salary, request, view=self)
        
        serializer = SalarySerializer(result_page_salary, many = True)
        return paginator.get_paginated_response(serializer.data)
    
    
    def post(self, request):
        
        serializer = SalarySerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SalaryDetailUpdateDelete(APIView):
    permission_classes = [AllowAny]
    def get_object(self, pk):
        
        try:
            salary = SalaryModel.objects.get(pk = pk)
            return salary
        except SalaryModel.DoesNotExist:
            return None
        
    
    def get(self, request, pk):
        
        salary = self.get_object(pk)
        
        if salary is None:
            return Response({"detail": "Salary not found"}, status=404)

        
        serializer = SalarySerializer(salary)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        
        salary = self.get_object(pk)
        
        if salary is None:
            return Response({"detail": "Salary not found"}, status=404)
        
        serializer = SalarySerializer(salary, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    
    
    def patch(self, request, pk):
        
        salary = self.get_object(pk)
        
        if salary is None:
            return Response({"detail": "Salary not found"}, status=404)
        
        serializer = SalarySerializer(salary, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        
        salary = self.get_object(pk)
        
        if salary is None:
            return Response({"detail": "Salary not found"}, status=404)

        
        salary.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    