from django.db import models

class cheakTable(models.Model):
    ids=models.IntegerField()
    name=models.CharField(max_length=25)
    dep=models.CharField(max_length=3)
    code=models.IntegerField()

class makePersionalDe(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    department=models.CharField(max_length=3)
    dep_code=models.IntegerField()
    password=models.IntegerField()
