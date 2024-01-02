# fixtures/load_data.py
import csv
from django.db import transaction
from .models import Fixture, HockeyClub

def load_data_from_csv(model, file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # Clear existing data in the model's table
        model.objects.all().delete()

        # Use Django's transaction.atomic() to ensure data consistency
        with transaction.atomic():
            for row in reader:
                # Create a model object for each row in the CSV
                obj = model(**row)
                obj.save()

def run():
    # Specify the path to your CSV files
    fixture_csv_path = 'fixtures.csv'
    hockeyclub_csv_path = 'locations.csv'

    # Load data from CSV into the Fixture model
    load_data_from_csv(Fixture, fixture_csv_path)

    # Load data from CSV into the HockeyClub model
    load_data_from_csv(HockeyClub, hockeyclub_csv_path)

# Call the run function when the script is executed
if __name__ == "__main__":
    run()
