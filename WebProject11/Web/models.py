from django.db import models

class FormEnteriesModel(models.Model):
    class Meta:
        db_table = 'ManualForm'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    rollno = models.IntegerField()
    category = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    state = models.CharField(max_length=15)
