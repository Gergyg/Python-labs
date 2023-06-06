from django.shortcuts import render, get_object_or_404, redirect
from .models import ServiceType
from .forms import ServiceTypeForm

def service_type_list(request):
    service_types = ServiceType.objects.all()
    return render(request, 'service_types/service_type_list.html', {'service_types': service_types})

def service_type_detail(request, pk):
    service_type = get_object_or_404(ServiceType, pk=pk)
    return render(request, 'service_types/service_type_detail.html', {'service_type': service_type})

def service_type_create(request):
    if request.method == 'POST':
        form = ServiceTypeForm(request.POST)
        if form.is_valid():
            service_type = form.save()
            return redirect('service_type_detail', pk=service_type.pk)
    else:
        form = ServiceTypeForm()
    return render(request, 'service_types/service_type_create.html', {'form': form})

def service_type_update(request, pk):
    service_type = get_object_or_404(ServiceType, pk=pk)
    if request.method == 'POST':
        form = ServiceTypeForm(request.POST, instance=service_type)
        if form.is_valid():
            service_type = form.save()
            return redirect('service_type_detail', pk=service_type.pk)
    else:
        form = ServiceTypeForm(instance=service_type)
    return render(request, 'service_types/service_type_update.html', {'form': form})

def service_type_delete(request, pk):
    service_type = get_object_or_404(ServiceType, pk=pk)
    if request.method == 'POST':
        service_type.delete()
        return redirect('service_type_list')
    return render(request, 'service_types/service_type_delete.html', {'service_type': service_type})
