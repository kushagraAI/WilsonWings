from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Destination

class DestinationAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.destination = Destination.objects.create(
            name='Existing Destination',
            country='Existing Country',
            description='A test destination.',
            best_time_to_visit='Summer',
            category='Beach',
            image='http://example.com/image.jpg'
        )

    def test_create_destination_authenticated(self):
        url = reverse('destination-list')
        data = {
            'name': 'New Destination',
            'country': 'New Country',
            'description': 'A new test destination.',
            'best_time_to_visit': 'Spring',
            'category': 'Mountain',
            'image': 'http://example.com/image.jpg'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Destination.objects.count(), 2)
        self.assertEqual(Destination.objects.get(id=response.data['id']).name, 'New Destination')

    def test_create_destination_unauthenticated(self):
        self.client.credentials()  # Remove token to simulate unauthenticated request
        url = reverse('destination-list')
        data = {
            'name': 'New Destination',
            'country': 'New Country',
            'description': 'A new test destination.',
            'best_time_to_visit': 'Spring',
            'category': 'Mountain',
            'image': 'http://example.com/image.jpg'
        }
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
        data = {
            'name': 'Updated Destination',
            'country': 'Updated Country',
            'description': 'Updated description.',
            'best_time_to_visit': 'Winter',
            'category': 'City',
            'image': 'http://example.com/updated_image.jpg'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.destination.refresh_from_db()
        self.assertEqual(self.destination.name, 'Updated Destination')
        self.assertEqual(self.destination.country, 'Updated Country')
        self.assertEqual(self.destination.description, 'Updated description.')
        self.assertEqual(self.destination.best_time_to_visit, 'Winter')
        self.assertEqual(self.destination.category, 'City')
        self.assertEqual(self.destination.image, 'http://example.com/updated_image.jpg')

    def test_update_destination_unauthenticated(self):
        self.client.credentials()  # Remove token to simulate unauthenticated request
        url = reverse('destination-detail', kwargs={'pk': self.destination.id})
        data = {
            'name': 'Updated Destination',
            'country': 'Updated Country',
            'description': 'Updated description.',
            'best_time_to_visit': 'Winter',
            'category': 'City',
            'image': 'http://example.com/updated_image.jpg'
        }
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
