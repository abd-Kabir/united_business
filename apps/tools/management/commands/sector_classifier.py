import pandas as pd

from django.conf import settings
from django.core.management import BaseCommand

from os.path import join as join_path

from apps.tools.models import SectorClassifier


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = join_path(settings.BASE_DIR, 'archive', 'sector_classifier.xlsx')
        df = pd.read_excel(path)

        clusters = []
        count = 1
        for index, row in df.iterrows():
            combined = row['tnved']
            tnved = combined.split(' ')[0].replace('.', '')
            short_name = ' '.join(combined.split(' ')[1:])
            trade_instance = SectorClassifier(
                mark=row['mark'],
                name=row['name'],
                short_name=short_name,
                tnved=tnved
            )
            clusters.append(trade_instance)
            count += 1
            print('COUNT: ', count)
        SectorClassifier.objects.bulk_create(clusters)
        print('FINISHED!')
        return "DONE"
