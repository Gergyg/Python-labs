from django.urls import path
from . import views

app_name = 'master_specializations'

urlpatterns = [
    path('', views.specialization_list, name='specialization_list'),
    path('<int:pk>/', views.specialization_detail, name='specialization_detail'),
    path('create/', views.specialization_create, name='specialization_create'),
    path('<int:pk>/update/', views.specialization_update, name='specialization_update'),
    path('<int:pk>/delete/', views.specialization_delete, name='specialization_delete'),
]
