from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Destination

class DestinationModelTest(TestCase):

    def test_create_destination(self):
        destination = Destination.objects.create(name="Test Destination", description="A test destination.")
        self.assertEqual(destination.name, "Test Destination")
        self.assertEqual(destination.description, "A test destination.")

    def test_name_cannot_be_blank(self):
        with self.assertRaises(ValidationError):
            destination = Destination(name="", description="A test destination.")
            destination.full_clean()  # This will trigger model validation
