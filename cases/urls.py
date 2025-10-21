from django.urls import path
from . import views

urlpatterns = [
    path('', views.case_list, name='case_list'),
    path('case/<int:pk>/', views.case_detail, name='case_detail'),
    path('add/', views.add_case, name='add_case'),
    path('update-status/<int:pk>/', views.update_case_status, name='update_case_status'),
    path('export/', views.export_cases_csv, name='export_cases_csv'),
    path('chart/', views.cases_chart, name='cases_chart'),
]
