# shopkeeper_project/shopkeeper/management/commands/import_electronics.py

import csv
from django.core.management.base import BaseCommand
from shopkeeper.models import Product

class Command(BaseCommand):
    help = 'Import electronic products from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Product.objects.update_or_create(
                    product_number=row['product_number'],
                    defaults={
                        'name': row['name'],
                        'selling_price': float(row['selling_price']),
                        'buying_price': float(row['buying_price'])
                    }
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported electronic products'))
