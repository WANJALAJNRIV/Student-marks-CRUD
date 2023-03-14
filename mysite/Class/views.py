from django.shortcuts import render, redirect
from .models import Class, ClassEnrollment
from .forms import NewClassForm, EditClassForm
from django.shortcuts import redirect, get_list_or_404, get_object_or_404


def list_classes(request):
    classes = Class.objects.all()
    context = {'classes': classes}
    return render(request, 'list_classes.html', context)


def add_class(request):
    context = {}
    form = NewClassForm()
    context = {'form': form}
    if request.method == 'POST':
        form  = NewClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_classes')
    return render(request, 'add_class.html', context)


def edit_class(request, id):
    _class = get_object_or_404(Class, id=id) 
    
    if request.method == 'POST':
        form  = EditClassForm(request.POST, instance=_class)
        if form.is_valid():
                form.save()
                return redirect('list_classes')
    else:
        form = EditClassForm(instance=_class)
        context={"form":form }
        return render(request, 'update_classes.html', context)
    return redirect('list_classes')

def delete_class(request, id):
    _class = get_object_or_404(Class, id=id)
    _class.delete()
    return redirect('list_classes')
    



