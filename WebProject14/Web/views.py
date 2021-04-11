from django.shortcuts import render
from .forms import EntryForm
from .models import EntryModel

# Create your views here.
def entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            rollno = form.cleaned_data['rollno']
            category = form.cleaned_data['category']
            classNumber = form.cleaned_data['classNumber']
                       
            form.save()
            return render(request, 'detail.html', {'name':name, 'rollno':rollno, 'category':category, 'classNumber': classNumber})
    else:
        form = EntryForm()
    return render(request, 'form.html', {'form': form})
