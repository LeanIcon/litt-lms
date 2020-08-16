from django.db import models

class Lms(models.Model):
        #name and alias character fields where strings are stored
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name

# Create your models here.
