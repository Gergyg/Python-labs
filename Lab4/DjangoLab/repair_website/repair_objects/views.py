from django.shortcuts import render, get_object_or_404, redirect
from .models import RepairObject
from .forms import RepairObjectForm

def repair_object_list(request):
    objects = RepairObject.objects.all()
    return render(request, 'repair_objects/repair_object_list.html', {'objects': objects})

def repair_object_detail(request, pk):
    object = get_object_or_404(RepairObject, pk=pk)
    return render(request, 'repair_objects/repair_object_detail.html', {'object': object})

def repair_object_create(request):
    if request.method == 'POST':
        form = RepairObjectForm(request.POST)
        if form.is_valid():
            object = form.save()
            return redirect('repair_object_detail', pk=object.pk)
    else:
        form = RepairObjectForm()
    return render(request, 'repair_objects/repair_object_create.html', {'form': form})

def repair_object_update(request, pk):
    object = get_object_or_404(RepairObject, pk=pk)
    if request.method == 'POST':
        form = RepairObjectForm(request.POST, instance=object)
        if form.is_valid():
            object = form.save()
            return redirect('repair_object_detail', pk=object.pk)
    else:
        form = RepairObjectForm(instance=object)
    return render(request, 'repair_objects/repair_object_update.html', {'form': form, 'object': object})

def repair_object_delete(request, pk):
    object = get_object_or_404(RepairObject, pk=pk)
    if request.method == 'POST':
        object.delete()
        return redirect('repair_object_list')
    return render(request, 'repair_objects/repair_object_delete.html', {'object': object})
