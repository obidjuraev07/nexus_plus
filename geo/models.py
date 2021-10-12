from django.db import models

# Create your models here.
class Region(models.Model):
    name_uz = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    ordering = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name_uz

class District(models.Model):
    name_uz = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    ordering = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name_uz