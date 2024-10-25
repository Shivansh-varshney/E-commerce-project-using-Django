# your_app/management/commands/populate_db.py

from django.core.management.base import BaseCommand
from core.factories import *
from core.models import Product
from userauths.models import User
from vendors.models import Vendor


class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **kwargs):
        # Create users
        # print("\nCreating Users...")
        # user = UserFactory.create_batch(20)
        # print("Done\n")

        # create vendors
        # print('\nCreating vendors...')
        # for user in User.objects.all()[2:12]:
        #     vendor = VendorFactory.create(user=user)
        # print('Vendors Created\n')

        #  create customer addresses
        # print('\nCreating Customer Address...')
        # for user in User.objects.all()[1:]:
        #     vendor = CustomerAddressFactory.create(user=user)
        # print('Customer Address Created\n')

        #  create vendor addresses
        # print('\nCreating Vendor Bank Details...')
        # for user in Vendor.objects.all():
        #     vendor = VendorBankDetailsFactory.create(vendor=user)
        # print('Vendor Bank Created\n')

        #  create vendor addresses
        # print('\nCreating Vendor Address...')
        # for user in Vendor.objects.all():
        #     vendor = VendorAddressFactory.create(vendor=user)
        # print('Vendor Address Created\n')

        #  create vendor addresses
        # print('\nCreating Vendor Address...')
        # for vendor in Vendor.objects.all():
        #     for user in User.objects.all():
        #         review = VendorReviewFactory.create(vendor=vendor, user=user)
        # print('Vendor Address Created\n')

        # category_titles = [
        #     'Food',
        #     'Tech',
        #     'Home',
        #     'Decor',
        #     'Men',
        #     'Women',
        #     'Kids',
        #     'Furniture'
        # ]

        # print("\nCreating Categoris...")
        # for title in category_titles:
        #     category = CategoryFactory.create(title=title)
        # print("Done\n")

        # print("\nCreating Product Reviews...")
        # for product in Product.objects.all():
        #     for i in range(10):
        #         review = ProductReviewFactory.create(product=product)
        # print("Done\n")

        # print("\nCreating Vendor Address...")
        # for vendor in Vendor.objects.all():
        #     review = VendorBankDetailsFactory.create(vendor=vendor)
        # print("Done\n")

        # change stock quantity
        # print('\nChanging Stock Quantity for all Products')
        # for product in Product.objects.all():
        #     product.stock_quantity = 1000
        #     product.save()
        # print('Stock Quantity for all products is now 1000\n')

        # adding users to groups

        print('\nAdding Users to customer group')
        # for user in User.objects.all()[]

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated the database with dummy data'))
