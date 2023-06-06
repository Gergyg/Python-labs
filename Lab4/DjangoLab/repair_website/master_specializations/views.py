from django.shortcuts import render, get_object_or_404, redirect
from .models import MasterSpecialization
from .forms import MasterSpecializationForm

def specialization_list(request):
    specializations = MasterSpecialization.objects.all()
    return render(request, 'master_specializations/specialization_list.html', {'specializations': specializations})

def specialization_detail(request, pk):
    specialization = get_object_or_404(MasterSpecialization, pk=pk)
    return render(request, 'master_specializations/specialization_detail.html', {'specialization': specialization})

def specialization_create(request):
    if request.method == 'POST':
        form = MasterSpecializationForm(request.POST)
        if form.is_valid():
            specialization = form.save()
            return redirect('specialization_detail', pk=specialization.pk)
    else:
        form = MasterSpecializationForm()
    return render(request, 'master_specializations/specialization_create.html', {'form': form})

def specialization_update(request, pk):
    specialization = get_object_or_404(MasterSpecialization, pk=pk)
    if request.method == 'POST':
        form = MasterSpecializationForm(request.POST, instance=specialization)
        if form.is_valid():
            specialization = form.save()
            return redirect('specialization_detail', pk=specialization.pk)
    else:
        form = MasterSpecializationForm(instance=specialization)
    return render(request, 'master_specializations/specialization_update.html', {'form': form, 'specialization': specialization})

def specialization_delete(request, pk):
    specialization = get_object_or_404(MasterSpecialization, pk=pk)
    if request.method == 'POST':
        specialization.delete()
        return redirect('specialization_list')
    return render(request, 'master_specializations/specialization_delete.html', {'specialization': specialization})
