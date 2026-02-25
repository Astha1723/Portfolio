from django.db import models

# Create your models here.
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):   # 👈 SAME LEVEL 
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name