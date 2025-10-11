from django.db import models

class Service(models.Model):
     SERVICE_TYPES = [
        ('health', 'Health'),
        ('finance', 'Finance'),
        ('registration', 'Registration'),
        ('clubs', 'Clubs & Societies'),
        ('ict', 'ICT'),
        ('other', 'Other'),
    ]
     
     name = models.CharField(max_length=100)
     type = models.CharField(max_length=20, choices=SERVICE_TYPES)
     office_location = models.CharField(max_length=200)
     description = models.TextField()
     contact = models.CharField(max_length=100, blank=True, null=True)
     opening_hours = models.CharField(max_length=100, blank=True, null=True)

     def __str__(self):
          return self.name
    
