from django.shortcuts import render, get_object_or_404, redirect
from .models import RepairCategory
from .forms import RepairCategoryForm

def category_list(request):
    categories = RepairCategory.objects.all()
    return render(request, 'repair_categories/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(RepairCategory, pk=pk)
    return render(request, 'repair_categories/category_detail.html', {'category': category})

def category_create(request):
    if request.method == 'POST':
        form = RepairCategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('category_detail', pk=category.pk)
    else:
        form = RepairCategoryForm()
    return render(request, 'repair_categories/category_create.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(RepairCategory, pk=pk)
    if request.method == 'POST':
        form = RepairCategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('category_detail', pk=category.pk)
    else:
        form = RepairCategoryForm(instance=category)
    return render(request, 'repair_categories/category_update.html', {'form': form, 'category': category})

def category_delete(request, pk):
    category = get_object_or_404(RepairCategory, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'repair_categories/category_delete.html', {'category': category})
