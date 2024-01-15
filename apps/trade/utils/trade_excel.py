import pandas as pd
from os.path import join as join_path
from django.conf import settings

from apps.trade.models import Trade


def export():
    base_dir = settings.BASE_DIR
    file_path = join_path(base_dir, 'archive', 'export.xlsx')
    df = pd.read_excel(file_path)

    batch_size = 10_000
    trades = []
    count = 1
    for index, row in df.iterrows():
        trade_instance = Trade(
            mode=row['mode'],
            country=row['country'],
            TNVED=row['TNVED'],
            category=row['category'],
            region=row['region'],
            stir_pinfl=row['stir'],
            organization=row['organization'],
            product=row['product'],
            unit=row['unit'],
            weight=row['weight'],
            quantity=row['quantity'],
            price=row['price'],
            date=row['date']
        )
        trades.append(trade_instance)
        if len(trades) >= batch_size:
            Trade.objects.bulk_create(trades)
            trades = []
        count += 1
        print('COUNT: ', count)
    if trades:
        Trade.objects.bulk_create(trades)
    print('FINISHED!')
    return "DONE"


def import_data():
    base_dir = settings.BASE_DIR
    file_path = join_path(base_dir, 'archive', 'import.xlsx')
    df = pd.read_excel(file_path)

    batch_size = 10_000
    trades = []
    count = 1
    for index, row in df.iterrows():
        trade_instance = Trade(
            mode=row['mode'],
            country=row['country'],
            TNVED=row['TNVED'],
            category=row['category'],
            region=row['region'],
            stir_pinfl=row['stir'],
            organization=row['organization'],
            product=row['product'],
            unit=row['unit'],
            weight=row['weight'],
            quantity=row['quantity'],
            price=row['price'],
            date=row['date']
        )
        trades.append(trade_instance)
        if len(trades) >= batch_size:
            Trade.objects.bulk_create(trades)
            trades = []
        count += 1
        print('COUNT: ', count)
    if trades:
        Trade.objects.bulk_create(trades)
    print('FINISHED!')
    return "DONE"

