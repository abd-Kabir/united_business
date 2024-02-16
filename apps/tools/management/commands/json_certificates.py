import json

from django.core.management import BaseCommand

from os.path import join as join_path

from apps.tools.models import Certificate
from config.settings import BASE_DIR


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = join_path(BASE_DIR, 'archive', 'certificates.json')
        with open(path, "r", encoding='utf-8-sig') as file:
            datas = json.load(file)
            for data in datas:
                district_id = data.get('soato')
                company_name = data.get('ccompany_name')
                stir = data.get('stir').replace(' ', '')
                industrial_networks = data.get('industrial_networks')
                product_name = data.get('product_name')
                quality_systems = data.get('quality_systems')
                Certificate.objects.create(
                    company_name=company_name,
                    stir=stir,
                    industrial_networks=industrial_networks,
                    product_name=product_name,
                    quality_systems=quality_systems,
                    district_id=district_id
                )
