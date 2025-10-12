from django.shortcuts import render
from .models import Location

def location_list(request):
    locations = Location.objects.all().order_by('name')
    return render(request, 'locations/location_list.html', {'locations': locations})
