from django.shortcuts import render, redirect, get_object_or_404

from .models import FormEnteriesModel
from .forms import EntryForm

def index(request):
    context = FormEnteriesModel.objects.all()
    return render(request, 'list.html', {'context': context})


def add(request):
    form = EntryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, 'add.html', context)


def edit(request, id):
    entry = get_object_or_404(FormEnteriesModel, id=id)
    form = EntryForm(request.POST or None, instance=entry)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, 'edit.html', context)


def delete(request, id):
    obj = get_object_or_404(FormEnteriesModel, id=id)

    if request.method == 'POST':
        obj.delete()
        return redirect('/')
    context = {"entry": obj}
    return render(request, 'delete.html', context)