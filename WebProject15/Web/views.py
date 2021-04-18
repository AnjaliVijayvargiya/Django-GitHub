from django.shortcuts import render
from .forms import EntryForm
from .models import EntryModel

# Create your views here.
def entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():

            body = {
            'name': form.cleaned_data['name'],
            'rollno': str(form.cleaned_data['rollno']),
            'category': form.cleaned_data['category'],
            'date': form.cleaned_data['date'],
            'time': form.cleaned_data['time'],
            'email': form.cleaned_data['email'],
            'favorite_color': form.cleaned_data['favorite_color'],
            'gender': form.cleaned_data['gender'],
            'description': form.cleaned_data['description']
			}

            name = form.cleaned_data['name']
            rollno = form.cleaned_data['rollno']
            category = form.cleaned_data['category']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            email = form.cleaned_data['email']
            favorite_color = form.cleaned_data['favorite_color']
            gender = form.cleaned_data['gender']
            description = form.cleaned_data['description']
            color = favorite_color[-1]

            body1 = {
            'name': name,
            'rollno': str(rollno),
            'category': category,
            'date': date,
            'time': time,
            'email': email,
            'favorite_color': favorite_color,
            'gender': gender,
            'description': description,
            'color': color
			}
           
            #print(body)
            #print(favorite_color)
            #print(color)

            form.save()
            return render(request, 'detail.html', body1)
    else:
        form = EntryForm()
    return render(request, 'form.html', {'form': form})