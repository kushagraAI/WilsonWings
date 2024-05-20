from django.urls import path,include
from rest_framework.routers import DefaultRouter
from destinations.views import DestinationViewSet,CustomAuthToken
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'destinations', DestinationViewSet)


urlpatterns = [
    
    path('', include(router.urls)),
    path('api-token-auth/', CustomAuthToken.as_view(), name= 'auth-token'),
]