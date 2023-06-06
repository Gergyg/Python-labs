from django.shortcuts import render, get_object_or_404, redirect
from .models import Sale
from .forms import SaleForm

def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sales/sale_list.html', {'sales': sales})

def sale_detail(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    return render(request, 'sales/sale_detail.html', {'sale': sale})

def sale_create(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save()
            return redirect('sale_detail', pk=sale.pk)
    else:
        form = SaleForm()
    return render(request, 'sales/sale_create.html', {'form': form})

def sale_update(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            sale = form.save()
            return redirect('sale_detail', pk=sale.pk)
    else:
        form = SaleForm(instance=sale)
    return render(request, 'sales/sale_update.html', {'form': form, 'sale': sale})

def sale_delete(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == 'POST':
        sale.delete()
        return redirect('sale_list')
    return render(request, 'sales/sale_delete.html', {'sale': sale})
