from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.views import ObtainJSONWebToken
from django.contrib.auth.models import User


class CustomObtainJWTView(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            token = response.data['token']
            user = self.user
            user_data = {
                'user_id': user.id,
                'username': user.username,
            }
            response.data = {
                'token': token,
                'user': user_data,
            }
        return response




