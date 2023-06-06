from django.urls import path
from . import views

app_name = 'service_types'

urlpatterns = [
    path('', views.service_type_list, name='service_type_list'),
    path('<int:pk>/', views.service_type_detail, name='service_type_detail'),
    path('create/', views.service_type_create, name='service_type_create'),
    path('<int:pk>/update/', views.service_type_update, name='service_type_update'),
    path('<int:pk>/delete/', views.service_type_delete, name='service_type_delete'),
]
