from django.shortcuts import render, get_object_or_404, redirect
from .forms import RepairForm
from .models import Repair
from customers.models import Customer
from django.db.models import Sum

def repair_list(request):
    repairs = Repair.objects.all()
    return render(request, 'repairs/repair_list.html', {'repairs': repairs})

def repair_detail(request, pk):
    repair = get_object_or_404(Repair, pk=pk)
    return render(request, 'repairs/repair_detail.html', {'repair': repair})

def repair_create(request):
    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            repair = form.save()
            return redirect('repair_detail', pk=repair.pk)
    else:
        form = RepairForm()
    return render(request, 'repairs/repair_form.html', {'form': form})

def repair_update(request, pk):
    repair = get_object_or_404(Repair, pk=pk)
    if request.method == 'POST':
        form = RepairForm(request.POST, instance=repair)
        if form.is_valid():
            repair = form.save()
            return redirect('repair_detail', pk=repair.pk)
    else:
        form = RepairForm(instance=repair)
    return render(request, 'repairs/repair_form.html', {'form': form})

def repair_delete(request, pk):
    repair = get_object_or_404(Repair, pk=pk)
    if request.method == 'POST':
        repair.delete()
        return redirect('repair_list')
    return render(request, 'repairs/repair_confirm_delete.html', {'repair': repair})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'repairs/customer_list.html', {'clients': customers})

def yearly_summary(request):
    summary = Repair.objects.values('date_completed__year').annotate(total_cost=Sum('part__price') + Sum('labour_cost'))
    return render(request, 'repairs/yearly_summary.html', {'summary': summary})
