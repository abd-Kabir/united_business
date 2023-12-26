import json
from os.path import join as join_path

from django.conf import settings
from django.core.management import BaseCommand

from apps.mapping.models import Country


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = join_path(settings.BASE_DIR, 'archive', 'country_id.json')
        with open(path, 'r', encoding='utf-8') as file:
            datas = json.load(file)
            count = 1
            for data in datas:
                Country.objects.filter(code=data.get('Code')).update(trade_name=data.get('Country'))
                print("COUNT: ", count)
                count += 1
