from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated, PermissionDenied, ValidationError
from rest_framework import status
from django.http import JsonResponse

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if response is None:
        if isinstance(exc, AuthenticationFailed):
            return JsonResponse(
                {"detail": "Invalid credentials provided."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        elif isinstance(exc, NotAuthenticated):
            return JsonResponse(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        elif isinstance(exc, PermissionDenied):
            return JsonResponse(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN
            )
        elif isinstance(exc, ValidationError):
            return JsonResponse(
                {"detail": exc.detail},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            return JsonResponse(
                {"detail": "An internal server error occurred."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    else:
        if isinstance(exc, AuthenticationFailed):
            response.data = {"detail": "Invalid credentials provided."}
        elif isinstance(exc, NotAuthenticated):
            response.data = {"detail": "Authentication credentials were not provided."}
        elif isinstance(exc, PermissionDenied):
            response.data = {"detail": "You do not have permission to perform this action."}

    return response
