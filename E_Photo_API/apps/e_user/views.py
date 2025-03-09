from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

from E_Photo_API.apps.e_user.serializers import UserRegistrationSerializer, \
                                                UserLoginSerializer

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

class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = authenticate(username=serializer.validated_data['username'],
                                password=serializer.validated_data['password']
            )

            if user is not None:
                print(request.user.password)
                auth_login(request, user)

                response = Response(status=status.HTTP_200_OK)
                response.set_cookie(
                    key='sessionid',
                    value=request.session.session_key,
                    httponly=True,  # Запобігає доступу до куки з JavaScript
                )
                print(response.cookies)
                return response
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

