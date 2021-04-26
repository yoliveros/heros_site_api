from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from heros_apis.serializers import UserSerializer

# Create your views here.


class UserApi(APIView):
    @classmethod
    def post(cls, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
