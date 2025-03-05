from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from E_Photo_API.apps.e_user.serializers import UserRegistrationSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_201_CREATED)

