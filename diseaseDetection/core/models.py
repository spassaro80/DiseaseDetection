from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=200, verbose_name = 'Category')

    def __str__(self):
        return str(self.pk) + " " + self.name
    
    class Meta:
        ordering = ["pk"]



class Symptom(models.Model):
    name=models.CharField(max_length=200, verbose_name = 'Symptom')
    category=models.ForeignKey(Category,on_delete=models.CASCADE, blank="True", null="True")

    def __str__(self):
        return self.name


class Disease(models.Model):
    name=models.CharField(max_length=200, verbose_name = 'Disease')
    description=models.TextField(verbose_name="description", blank="True", null="True")
    symptoms=models.ManyToManyField(Symptom, blank="True")

    def __str__(self):
        return self.name

class Survey(models.Model):
    disease=models.ForeignKey(Disease,on_delete=models.CASCADE, blank="True", null="True")
    description=models.TextField(verbose_name="description", blank="True", null="True")
    symptoms=models.ManyToManyField(Symptom, blank="True")
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank="True", null="True")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (F"Survey submitted by {self.user.username} on {datetime.date(self.created)}")