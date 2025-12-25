from rest_framework import renderers
import json

class UnifiedJSONRenderer(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context.get('response')
        status_code = response.status_code

        if isinstance(data, dict) and 'status' in data:
            return super().render(data, accepted_media_type, renderer_context)

        status_text = 'success' if status_code < 400 else 'error'
        
        message = ""
        if status_text == 'error':
            if isinstance(data, dict) and 'detail' in data:
                message = data.pop('detail')
            elif isinstance(data, dict) and 'non_field_errors' in data:
                message = data.pop('non_field_errors')[0]
            else:
                message = "An error occurred while processing your request."
        else:
            message = "Operation completed successfully."

        unified_data = {
            'status': status_text,
            'message': message,
            'data': data
        }

        return super().render(unified_data, accepted_media_type, renderer_context)
