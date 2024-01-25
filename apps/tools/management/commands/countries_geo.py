import json
from os.path import join as join_path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry

from apps.mapping.models import Country


class Command(BaseCommand):
    help = 'Import countries from GeoJSON file'

    def handle(self, *args, **options):
        path = join_path(settings.BASE_DIR, 'archive', 'countries.geojson')
        with open(path, 'r') as file:
            data = json.load(file)
            countries = []
            for feature in data['features']:
                name = feature['properties']['ADMIN']
                code = feature['properties']['ISO_A3']
                geometry = GEOSGeometry(json.dumps(feature['geometry']))

                country = Country(name=name, geometry=geometry, code=code)
                countries.append(country)

                self.stdout.write(self.style.SUCCESS(f'Successfully imported {name}'))
            Country.objects.bulk_create(countries)
            self.stdout.write(self.style.SUCCESS(f'Successfully DONE!'))
