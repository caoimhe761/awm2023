# fixtures/urls.py
from django.urls import path
from .views import upcoming_fixtures

urlpatterns = [
    path('', upcoming_fixtures, name='fixtures'),
]
