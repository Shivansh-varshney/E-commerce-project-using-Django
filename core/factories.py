import factory
import requests
from .models import *
from userauths.models import *
from vendors.models import *
from io import BytesIO
from faker import Faker
from userauths.models import User
from django.core.files.base import ContentFile
from django.contrib.auth.hashers import make_password

fake = Faker()


def get_image_from_url(url):
    response = requests.get(url)
    return ContentFile(BytesIO(response.content).read(), name='temp.jpg')


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.LazyFunction(lambda: make_password('admin'))


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.LazyAttribute(lambda x: fake.word())
    image = factory.LazyAttribute(
        lambda x: get_image_from_url(fake.image_url()))


class CustomerAddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomerAddress

    # Create a User factory or replace with an existing user
    user = factory.SubFactory(UserFactory)
    addressname = factory.Faker('word')
    housenumber = factory.Faker('building_number')
    landmark = factory.Faker('word')
    street = factory.Faker('street_name')
    city = factory.Faker('city')
    district = factory.Faker('city')
    state = factory.Faker('state')
    country = factory.Faker('country')
    zipcode = factory.Faker('postcode')
    status = factory.Faker('boolean')


class VendorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vendor

    user = factory.SubFactory(UserFactory)
    title = factory.LazyAttribute(lambda x: fake.company())
    image = factory.LazyAttribute(
        lambda x: get_image_from_url(fake.image_url()))
    description = factory.LazyAttribute(lambda x: fake.text())


class VendorAddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = vendorAddress

    # Create a User factory or replace with an existing user
    vendor = factory.SubFactory(VendorFactory)
    floornumber = factory.Faker('building_number')
    building = factory.Faker('word')
    street = factory.Faker('street_name')
    city = factory.Faker('city')
    district = factory.Faker('city')
    state = factory.Faker('state')
    country = factory.Faker('country')
    zipcode = factory.Faker('postcode')


class VendorBankDetailsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = vendorBankDetails

    vendor = factory.SubFactory(VendorFactory)
    bank_name = factory.Faker('company')
    account_holder_name = factory.Faker('name')
    account_number = factory.Faker(
        'random_int', min=1000000, max=2147483647)
    account_type = factory.Faker(
        'random_element', elements=['Savings', 'Current'])
    ifsc = factory.Faker('bothify', text='????0#####')
    branch_address = factory.Faker('address')
    pan_number = factory.Faker('bothify', text='?????#####')
    gst_number = factory.Faker('bothify', text='##?????###?#')
    cin = factory.Faker('bothify', text='L######')


class VendorReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = vendor_review

    user = factory.Iterator(User.objects.all())
    vendor = factory.Iterator(Vendor.objects.all())

    description = factory.LazyAttribute(lambda x: fake.text())
    date = factory.Faker('date_time_this_year')
    rating = factory.Faker('random_int', min=1, max=5)


class ProductReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductReview

    user = factory.Iterator(User.objects.all())  # Selects an existing user
    # Selects an existing product
    product = factory.Iterator(Product.objects.all())
    review = factory.Faker('text')
    rating = factory.Faker('random_int', min=1, max=5)
    date = factory.Faker('date_time_this_year')
