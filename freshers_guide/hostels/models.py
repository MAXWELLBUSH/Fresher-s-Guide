from django.db import models

class Hostel(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
