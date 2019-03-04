import json

from django.conf import settings
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from api.utils import encrypt, decrypt


class CustomMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if hasattr(response, 'data') and settings.ENCRYPT:
            response.data = encrypt(response.data)
            response.content = json.dumps(response.data)
        return response

    def process_request(self, request):
        if request.method == 'POST' and settings.DECRYPT:
            request.POST = {'data': json.dumps(decrypt(request.POST.get('data', '')))}
        return None
