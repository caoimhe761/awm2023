# your_app/urls.py
from django.urls import path
from .views import ClubsDetailView, update_club, DeleteClubView, add_club
import uuid


urlpatterns = [
    path('', ClubsDetailView.as_view(), name='clubs-detail'),
    path('add_club/', add_club, name='add_club'),
    path('update_club/<int:club_id>/', update_club, name='update_club'),
    path('delete_club/<int:club_id>/', DeleteClubView.as_view(), name='delete_club'),
]