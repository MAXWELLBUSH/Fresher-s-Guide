from django.shortcuts import render, get_object_or_404
from .models import Hostel

def hostel_list(request):
    hostels = Hostel.objects.all()
    return render(request, 'hostels/hostel_list.html', {'hostels': hostels})

def hostel_detail(request, pk):
    hostel = get_object_or_404(Hostel, pk=pk)
    return render(request, 'hostels/hostel_detail.html', {'hostel': hostel})
