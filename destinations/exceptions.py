from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    # Call the default exception handler first
    response = exception_handler(exc, context)

    # Now add the custom error handling
    if response is not None:
        custom_response_data = {
            'error': True,
            'status_code': response.status_code,
            'details': response.data,
        }
        response.data = custom_response_data

    # Handle exceptions that are not caught by DRF's default handler
    else:
        custom_response_data = {
            'error': True,
            'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'details': str(exc),
        }
        response = Response(custom_response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
