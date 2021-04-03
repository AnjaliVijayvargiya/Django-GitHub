from django.db import models

# Create your models here.
class EntryModel(models.Model):
  
    # fields of the model
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    rollno = models.IntegerField()
    category = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    state = models.CharField(max_length=15)
  
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.name