from django.db import models

class Location(models.Model):
    LOCATION_TYPES = [
        ('Lecture Hall', 'Lecture Hall'),
        ('Library', 'Library'),
        ('Cafeteria', 'Cafeteria'),
        ('Office', 'Office'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=LOCATION_TYPES)
    description = models.TextField(blank=True)
    block = models.CharField(max_length=50, blank=True)
    floor = models.CharField(max_length=20, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    hours = models.CharField(max_length=100, blank=True)
    map_link = models.URLField(blank=True)

    def __str__(self):
        return self.name
