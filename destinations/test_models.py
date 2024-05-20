from django.test import TestCase
from .models import Destination

class DestinationModelTest(TestCase):

    def test_create_destination(self):
        destination = Destination.objects.create(
            name='Test Destination',
            country='Test Country',
            description='A test destination description.',
            best_time_to_visit='Spring',
            category='Beach',
            image='http://example.com/image.jpg'
        )
        self.assertEqual(destination.name, 'Test Destination')
        self.assertEqual(destination.country, 'Test Country')
        self.assertEqual(destination.description, 'A test destination description.')
        self.assertEqual(destination.best_time_to_visit, 'Spring')
        self.assertEqual(destination.category, 'Beach')
        self.assertEqual(destination.image, 'http://example.com/image.jpg')

    def test_name_cannot_be_blank(self):
        with self.assertRaises(ValueError):
            Destination.objects.create(
                name='',
                country='Test Country'
            )

    def test_country_cannot_be_blank(self):
        with self.assertRaises(ValueError):
            Destination.objects.create(
                name='Test Destination',
                country=''
            )

    def test_str_representation(self):
        destination = Destination.objects.create(
            name='Test Destination',
            country='Test Country'
        )
        self.assertEqual(str(destination), destination.name)
