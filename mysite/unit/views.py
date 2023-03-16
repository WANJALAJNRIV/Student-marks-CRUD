#Wanjala Stephen David
# IN16/00055/20

from django.shortcuts import render, redirect
from .models import Unit
from .forms import NewUnitForm, EditUnitForm
from django.shortcuts import redirect, get_list_or_404, get_object_or_404


def list_units(request):
    units = Unit.objects.all()
    context = {'units': units}
    return render(request, 'list_units.html', context)


def add_unit(request):
    context = {}
    form = NewUnitForm()
    context = {'form': form}
    if request.method == 'POST':
        form  = NewUnitForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect('list_units')
    return render(request, 'add_unit.html', context)


def edit_unit(request, id):
    unit= get_object_or_404(Unit, id=id) 
    
    if request.method == 'POST':
        form  = EditUnitForm(request.POST, instance=unit)
        if form.is_valid():
                form.save()
                return redirect('list_units')
    else:
        form = EditUnitForm(instance=unit)
        context={"form":form }
        return render(request, 'update_unit.html', context)
    return redirect('list_units')

def delete_unit(request, id):
    unit = get_object_or_404(Unit, id=id)
    unit.delete()
    return redirect('list_units')




