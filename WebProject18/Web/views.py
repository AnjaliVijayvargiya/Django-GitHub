from django.shortcuts import render, HttpResponseRedirect
from .forms import EntryForm
from .models import EntryModel
from django.views.generic.base import TemplateView

# Create your views here.
class EntryView(TemplateView):
    template_name = 'form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = EntryForm()
        context = {'form':form}
        return context

    def post(self,request):
        form = EntryForm(request.POST)
        if form.is_valid():
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
            
            form.save()
            return render(request,'detail.html',body1)
        return render(request, 'form.html', {'form': form})