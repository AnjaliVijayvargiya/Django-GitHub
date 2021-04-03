from .models import EntryModel

from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.
from django.views.generic.list import ListView
  
class GeeksList(ListView):
  
    # specify the model for list view
    model = EntryModel

    template_name = os.path.join(BASE_DIR,"templates\\list.html")
    print(template_name,"helllloooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")

    #template_name = "Web/geeksmodel_list1.html"

from django.views.generic.edit import CreateView

class GeeksCreate(CreateView):
  
    # specify the model for create view
    model = EntryModel
    template_name = os.path.join(BASE_DIR,"templates\\add.html")
  
    # specify the fields to be displayed
    fields = ['name', 'rollno', 'category', 'gender','state']

    success_url ="/"

from django.views.generic.detail import DetailView
  
class GeeksDetailView(DetailView):
    # specify the model to use
    model = EntryModel
    template_name = os.path.join(BASE_DIR,"templates\\detail.html")

from django.views.generic.edit import UpdateView
  
class GeeksUpdateView(UpdateView):
    # specify the model you want to use
    model = EntryModel
  
    template_name = os.path.join(BASE_DIR,"templates\\add.html")
  
    # specify the fields to be displayed
    fields = ['name', 'rollno', 'category', 'gender','state']

    success_url ="/"

from django.views.generic.edit import DeleteView
  
class GeeksDeleteView(DeleteView):
    # specify the model you want to use
    model = EntryModel

    template_name = os.path.join(BASE_DIR,"templates\\delete.html")
    
    success_url ="/"
