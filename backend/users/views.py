from django.http import HttpResponseRedirect
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken
from .models import *


@api_view(['GET'])
def current_user(request):
    return Response(UserSerializer(request.user).data)


class UserList (APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response([UserSerializer(user).data for user in CustomUser.objects.all()])
