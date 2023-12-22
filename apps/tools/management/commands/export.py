from django.core.management import BaseCommand

from apps.trade.utils.trade_excel import export


class Command(BaseCommand):
    def handle(self, *args, **options):
        export()
