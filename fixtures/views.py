import requests
from django.shortcuts import render
from django.utils import timezone
from .models import Fixture

def upcoming_fixtures(request):
    # Assuming 'venue' is the attribute name in your Fixture model
    venues = Fixture.objects.values_list('venue', flat=True)
    
    # processed_venues = set()  # Keep track of processed venues

    # for venue in venues:
    #     if venue not in processed_venues:
    #         response = requests.get(f'http://localhost:8000/get-coordinates/?place={venue}')
        
    #         if response.status_code == 200:
    #             try:
    #                 data = response.json()
    #                 # Process the data as needed
    #                 latitude = data.get('latitude', None)
    #                 longitude = data.get('longitude', None)
                    
    #                 # Use latitude and longitude as needed
                    
    #                 # Add the venue to the set of processed venues
    #                 processed_venues.add(venue)
    #             except requests.exceptions.JSONDecodeError:
    #                 # Handle the case where the response is not valid JSON
    #                 print(f"Invalid JSON response for {venue}")
    #         else:
    #             # Handle non-200 status codes
    #             print(f"Request failed with status code: {response.status_code}")

    upcoming_fixtures = Fixture.objects.order_by('date', 'time')
    return render(request, 'fixtures.html', {'upcoming_fixtures': upcoming_fixtures})
