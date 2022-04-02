from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name

class Task(models.Model):
    name=models.CharField(max_length=250)
    review=models.IntegerField()


    def __str__(self):
        return self.name
