from django.urls import path
from . import views

urlpatterns = [
    path('repairs/', views.repair_list, name='repair_list'),
    path('repairs/<int:pk>/', views.repair_detail, name='repair_detail'),
    path('repairs/create/', views.repair_create, name='repair_create'),
    path('repairs/<int:pk>/update/', views.repair_update, name='repair_update'),
    path('repairs/<int:pk>/delete/', views.repair_delete, name='repair_delete'),
    path('customers/', views.customer_list, name='customer_list'),
    path('yearly-summary/', views.yearly_summary, name='yearly_summary'),
]
