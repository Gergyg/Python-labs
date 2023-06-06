from django.shortcuts import render, get_object_or_404, redirect
from .models import Master
from .forms import MasterForm

def master_list(request):
    masters = Master.objects.all()
    return render(request, 'masters/master_list.html', {'masters': masters})

def master_detail(request, pk):
    master = get_object_or_404(Master, pk=pk)
    return render(request, 'masters/master_detail.html', {'master': master})

def master_create(request):
    if request.method == 'POST':
        form = MasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('master_list')
    else:
        form = MasterForm()
    return render(request, 'masters/master_create.html', {'form': form})

def master_update(request, pk):
    master = get_object_or_404(Master, pk=pk)
    if request.method == 'POST':
        form = MasterForm(request.POST, instance=master)
        if form.is_valid():
            form.save()
            return redirect('master_list')
    else:
        form = MasterForm(instance=master)
    return render(request, 'masters/master_update.html', {'form': form})

def master_delete(request, pk):
    master = get_object_or_404(Master, pk=pk)
    if request.method == 'POST':
        master.delete()
        return redirect('master_list')
    return render(request, 'masters/master_delete.html', {'master': master})
