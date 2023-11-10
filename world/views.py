from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render
from .models import WorldBorder
import folium
from folium import plugins
# Create your views here.


def home(request):
    
    data = WorldBorder.objects.all()
    data_list = WorldBorder.objects.values_list('lat', 'lon', 'pop2005')
    filtered_data = [(lat, lon, value) for lat, lon, value in data_list if lat is not None and lon is not None]
    map1 = folium.Map(location=[19, -12],
                      tiles='CartoDB Dark_Matter', zoom_start=2)
    plugins.HeatMap(filtered_data).add_to(map1)
    plugins.Fullscreen(position='topright').add_to(map1)
    map1 = map1._repr_html_()
    
    context = {
        'map1': map1
    }
    return render(request, 'home.html', context)

