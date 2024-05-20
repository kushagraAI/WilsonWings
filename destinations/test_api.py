from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Destination

class DestinationAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.destination = Destination.objects.create(name="Existing Destination", description="A test destination.")


    def test_create_destination_unauthenticated(self):
        self.client.credentials()  # Remove token to simulate unauthenticated request
        url = reverse('destination-list')
        data = {'name': 'New Destination', 'description': 'A new test destination.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_destinations(self):
        url = reverse('destination-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.destination.name)

    def test_update_destination_authenticated(self):
        url = reverse('destination-detail', kwargs={'pk': self.destination.id})
        data = {'name': 'Updated Destination', 'description': 'Updated description.'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.destination.refresh_from_db()
        self.assertEqual(self.destination.name, 'Updated Destination')
        self.assertEqual(self.destination.description, 'Updated description.')

    def test_update_destination_unauthenticated(self):
        self.client.credentials()  # Remove token to simulate unauthenticated request
        url = reverse('destination-detail', kwargs={'pk': self.destination.id})
        data = {'name': 'Updated Destination', 'description': 'Updated description.'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_destination_authenticated(self):
        url = reverse('destination-detail', kwargs={'pk': self.destination.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Destination.objects.count(), 0)

    def test_delete_destination_unauthenticated(self):
        self.client.credentials()  # Remove token to simulate unauthenticated request
        url = reverse('destination-detail', kwargs={'pk': self.destination.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
