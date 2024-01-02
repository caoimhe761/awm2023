from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,  get_object_or_404, redirect
from rest_framework.generics import ListAPIView
from .models import SportsFacility
from django.views import View
from .forms import SportsFacilityForm

def add_club(request):
    if request.method == 'POST':
        # Extract data from the request.POST dictionary
        name = request.POST.get('Name')
        club_type = request.POST.get('Type')
        address = request.POST.get('Address')
        telephone = request.POST.get('Telephone')
        web = request.POST.get('Web')
        streetview = request.POST.get('Streetview')
        wgs84_longi = request.POST.get('WGS84Longi')
        wgs4_latitu = request.POST.get('WGS4Latitu')
        eircode = request.POST.get('Eircode')

        # Create a new SportsFacility instance and save it
        new_club = SportsFacility(
            Name=name,
            Type=club_type,
            Address=address,
            Telephone=telephone,
            Web=web,
            Streetview=streetview,
            WGS84Longi=wgs84_longi,
            WGS4Latitu=wgs4_latitu,
            Eircode=eircode
        )
        new_club.save()

        return redirect('clubs-detail')
    else:
        # Render the template for displaying the form
        return redirect('clubs-detail')

class ClubsDetailView(ListAPIView):
    template_name = 'clubs_detail.html'  # Update with your actual app name

    def get_queryset(self):
        return SportsFacility.objects.all()

    def get(self, request, *args, **kwargs):
        clubs = self.get_queryset()
        return render(request, self.template_name, {'clubs': clubs})

def home(request):
    data = SportsFacility.objects.all()
    context = {
        'data': data,
    }

    return render(request, 'home.html', context)


def update_club(request, club_id):
    
    # Retrieve the club object
    club = get_object_or_404(SportsFacility, OBJECTID=club_id)
    print(request.POST)
    if request.method == 'POST':
        print("test")
        print(request.POST)
        
        # Update club fields with the new values
        club.Name = request.POST.get('Name')
        club.Type = request.POST.get('Type')
        club.Address = request.POST.get('Address')
        club.Telephone = request.POST.get('Telephone')
        club.Web = request.POST.get('Web')
        club.Streetview = request.POST.get('Streetview')
        club.WGS84Longi = float(request.POST.get('WGS84Longi'))
        club.WGS4Latitu = float(request.POST.get('WGS4Latitu'))
        club.Eircode = request.POST.get('Eircode')

        print(club.Name)
        print(club)
            # Save the updated club
        club.save()

        return redirect('clubs-detail') 
    return redirect('clubs-detail') 
class DeleteClubView(View):
    def post(self, request, club_id):  # Add self as the first parameter
        # Retrieve the club object
        club = get_object_or_404(SportsFacility, OBJECTID=club_id)

        # Delete the club
        club.delete()

        # Redirect to the desired page after deletion
        return redirect('clubs-detail')  

