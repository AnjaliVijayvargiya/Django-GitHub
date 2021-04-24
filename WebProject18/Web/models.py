from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class EntryModel(models.Model):
  
    # fields of the model
    name = models.CharField(max_length=150)
    rollno = models.IntegerField()
    category = models.CharField(max_length=10)
    email = models.EmailField(null=True)
    gender = models.CharField(max_length=6,null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    
    FAVORITE_COLORS_CHOICES = [('Blue', 'Blue'),('Green', 'Green'), ('Black', 'Black'), ('Red','Red'),('White','White')]
    favorite_color = MultiSelectField(choices=FAVORITE_COLORS_CHOICES,null=True)

    description = models.CharField(max_length=200, null=True)
  
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.name