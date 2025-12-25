from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def unified_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_data = {
            'status': 'error',
            'message': 'Validation failed or permission denied.',
            'data': response.data
        }

        if 'detail' in response.data:
            custom_data['message'] = response.data.get('detail')

        response.data = custom_data
    else:
        pass

    return response
