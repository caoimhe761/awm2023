from django.shortcuts import render
from .models import Location
# Create your views here.


def home(request):
   
    data = Location.objects.all()
    # print(data)
    context = {
        'data': data,
    }

    return render(request, 'home.html', context)

from django.http import JsonResponse
from geopy.geocoders import Nominatim

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


