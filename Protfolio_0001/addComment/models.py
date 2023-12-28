from django.db import models

class addComment(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    topic_name=models.CharField(max_length=500)
    describe=models.TextField()
