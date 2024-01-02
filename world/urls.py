from django.urls import path
from . import views
from .views import get_coordinates
urlpatterns = [
    path('world/', views.home, name="home"),
    path('get-coordinates/', get_coordinates, name='get_coordinates'),
]