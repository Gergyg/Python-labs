from django.urls import path
from . import views

app_name = 'repair_objects'

urlpatterns = [
    path('', views.repair_object_list, name='repair_object_list'),
    path('<int:pk>/', views.repair_object_detail, name='repair_object_detail'),
    path('create/', views.repair_object_create, name='repair_object_create'),
    path('<int:pk>/update/', views.repair_object_update, name='repair_object_update'),
    path('<int:pk>/delete/', views.repair_object_delete, name='repair_object_delete'),
]
