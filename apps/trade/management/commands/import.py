from django.core.management import BaseCommand

from apps.trade.utils.trade_excel import import_data


class Command(BaseCommand):
    def handle(self, *args, **options):
        import_data()
