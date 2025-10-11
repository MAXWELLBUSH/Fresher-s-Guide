from django.shortcuts import render
from .models import Service


def services_list(request):
    services =  Service.objects.all().order_by('type', 'name')
    return render(request, 'services/services_list.html', {'services':services,})
