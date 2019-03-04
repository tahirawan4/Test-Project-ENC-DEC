from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response

from api.utils import encrypt, decrypt


class TestView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, pk=None):
        try:
            data = json.loads(request.POST.get('data'))
        except Exception as e:
            data = {"error": "Data is not json serializable"}
        return Response(data, status=status.HTTP_200_OK)
