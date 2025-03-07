from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User, Group

from E_Photo_API.apps.e_user.serializers import UserRegistrationSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = User.objects.create_user(
                username=serializer.data['username'],
                password=serializer.data['password'],
                email=serializer.data['email']
            )

            group, created = Group.objects.get_or_create(name=serializer.data['groups'][0])

            user.groups.add(group)
            user.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

