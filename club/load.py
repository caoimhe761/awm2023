from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import SportsFacility
sports_facilities_mapping = {
    'Name': 'Name',
    'Type': 'Type',
    'Address': 'Address',
    'Telephone': 'Telephone',
    'Web': 'Web',
    'Streetview': 'Streetview',
    'WGS84Longi': 'WGS84Longi',
    'WGS4Latitu': 'WGS4Latitu',
    'Eircode': 'Eircode',
    'geometry': 'POINT',  # Assuming your geometry field is a PointField
}



sports_facilities_shp = Path('C:/Users/caoim/OneDrive - Technological University Dublin/College/4th year/web map/labs/Sports_Facilities_-_Roscommon/Sports_Facilities.shp')

def run(verbose=True):
    lm = LayerMapping(SportsFacility, sports_facilities_shp, sports_facilities_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
