# fixtures/fetch_fixtures.py
import requests
from bs4 import BeautifulSoup
from .models import Fixture, Location
import json
from datetime import datetime
from django.db import connection
from geopy.geocoders import Nominatim


class GetHockeyLink:
    def __init__(self):
        self.team_urls = [
            {"url": "https://www.leinsterhockey.ie/league/184891/", "team": "Old Alexandra 4th"},
            {"url": "https://www.leinsterhockey.ie/league/184887/", "team": "Old Alexandra 2nd"},
            {"url": "https://www.leinsterhockey.ie/league/184888/", "team": "Old Alexandra 3rd"}
        ]
        self.fixture_list = []
        self.teams_points_list = []

    def GetSourceCode(self):
        for team_info in self.team_urls:
                    self.api_url = team_info["url"]
                    response = requests.get(self.api_url)

                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, "html.parser")
                        with open("soup_output.html", "w", encoding="utf-8") as file:
                            file.write(str(soup))
                        self.ExtractData(soup, team_info["team"])
                        self.SaveToDatabase()
                    else:
                        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return self     
    def ExtractData(self, soup, Old_alex_name):
        
        division_text = soup.find('div', class_='tag-label').get_text(strip=True)   
        teams_points = {}
        for team_row in soup.select(".table tbody tr"):
            team_name = team_row.select_one(".Team").get_text(strip=True)
            team_points = team_row.select_one(".Pts").get_text(strip=True)
                        
            # Convert team_points to integer (assuming it's a valid integer)
            try:
                team_points = int(team_points)
            except ValueError:
                # Handle the case where team_points is not a valid integer
                team_points = 0  # or any default value you prefer
            if team_name and team_points:
                teams_points[team_name] = team_points
                team_info = {
                    "league": division_text,
                    "team": team_name,
                    "points": team_points
                }
                self.teams_points_list.append(team_info)
     
        for fixture_row in soup.select(".table-body.fixtures"):
            teams_involved = [team.text.strip() for team in fixture_row.select(".fteam1 a, .fteam2 a")]
            if Old_alex_name in teams_involved:
                # Extracting date
                date_element = fixture_row.select_one(".largeview-hide.ftime .data")
                date = date_element.text.strip() if date_element else "Date not available"
                date_object = datetime.strptime(date, "%d %b %Y").date()
                # Extracting venue
                venue_element = fixture_row.select_one(".expand-item.largeview-hide label:-soup-contains('Venue')")
                venue = venue_element.text.split(':')[1].strip() if venue_element else "Venue not available"

                team1 = fixture_row.select_one(".fteam1 a").text.strip()
                team2 = fixture_row.select_one(".fteam2 a").text.strip()
                time = fixture_row.select_one(".fvs .data").text.strip()

                
                fixture_info = {
                    "league":division_text,
                    "date": date_object,
                    "time": time,
                    "team1": team1,
                    "team2": team2,
                    "venue": venue
                }

                self.fixture_list.append(fixture_info)


    def SaveToDatabase(self):
        Fixture.objects.all().delete()
        # Location.objects.all().delete()
        with connection.cursor() as cursor:
            # Clear existing data in the Fixture table and reset the id sequence
            cursor.execute("TRUNCATE TABLE fixtures_fixture RESTART IDENTITY;")

        
        for fixture in self.fixture_list:
            venue_name = fixture["venue"]
            geolocator = Nominatim(user_agent="world")
            location = geolocator.geocode(venue_name)

            # Assuming 'Fixture' is your Django model
            new_fixture = Fixture(
                team_name1=fixture["team1"],
                team_name2=fixture["team2"],
                date=fixture["date"],
                time=fixture["time"],
                venue=fixture["venue"],
                league=fixture["league"]
            )
            new_fixture.save()

hockey_link_instance = GetHockeyLink()

# Call the GetSourceCode method on the instance
hockey_link_instance.GetSourceCode()
