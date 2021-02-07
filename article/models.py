from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=10)


class Person(models.Model):
    name = models.CharField(max_length=10)
    id_number = models.CharField(max_length=15)
    department = models.ForeignKey(Department, related_name='member', on_delete=models.CASCADE)


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=50000)
    author = models.ManyToManyField(Person, related_name='wrote')
    editor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='edited')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='article')
