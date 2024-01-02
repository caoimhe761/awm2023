from django.shortcuts import render
from .models import Location
from club.models import SportsFacility
from django.http import JsonResponse
from geopy.geocoders import Nominatim
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def home(request):
    data = Location.objects.all()
    sports_facilities = SportsFacility.objects.all()
    context = {
        'data': data,
        'sports_facilities': sports_facilities,
    }

    return render(request, 'home.html', context)
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def get_coordinates(request):
    if request.method == 'GET':
        place = request.GET.get('place', '')
        geolocator = Nominatim(user_agent="world") 
        location = geolocator.geocode(place)

        if location:
            coordinates = {
                'latitude': location.latitude,
                'longitude': location.longitude,
            }
            Location.objects.create(place_name=place, latitude=location.latitude, longitude=location.longitude)
            return JsonResponse(coordinates)
        else:
            return JsonResponse({'error': 'Location not found'}, status=400)