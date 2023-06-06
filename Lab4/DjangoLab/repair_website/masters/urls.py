from django.urls import path
from . import views

app_name = 'masters'

urlpatterns = [
    path('', views.master_list, name='master_list'),
    path('<int:pk>/', views.master_detail, name='master_detail'),
    path('create/', views.master_create, name='master_create'),
    path('update/<int:pk>/', views.master_update, name='master_update'),
    path('delete/<int:pk>/', views.master_delete, name='master_delete'),
]
