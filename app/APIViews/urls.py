from django.urls import path
from APIViews.views import EmployeeListCreateView, EmployeeDetailUpdateDelete, BranchListCreateView, BranchDetailUpdateDelete, SalaryListCreateView, SalaryDetailUpdateDelete



urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name = "employee-list-create" ),
    path('employees/<int:pk>/', EmployeeDetailUpdateDelete.as_view(), name = 'emp-detail-update-delete'),
    
    path('branches/', BranchListCreateView.as_view(), name="branch-list-create"),
    path('branches/<int:pk>/', BranchDetailUpdateDelete.as_view(), name = "branch-detail-up-del"),
    
    path('salary/', SalaryListCreateView.as_view(), name = 'salary-list-create' ),
    path('salary/<int:pk>/', SalaryDetailUpdateDelete.as_view(), name='salary-detail-up-del')
    
    
]
