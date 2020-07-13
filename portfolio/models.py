from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=128)
    url = models.URLField()
    description = models.CharField(max_length=256)
    image = models.ImageField()

    def __str__(self):
        return self.title

