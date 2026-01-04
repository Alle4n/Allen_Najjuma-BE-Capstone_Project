from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        # Add custom formatting if desired
        response.data['status_code'] = response.status_code
    else:
        # Fallback for unhandled exceptions
        response = Response({
            'detail': 'Internal server error',
            'status_code': 500
        }, status=500)

    return response
