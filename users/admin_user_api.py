from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


from users.admin_serializer import AdminUserSerializer, AdminLoginSerializer
from users.models import MtAdminUser as Admin

class UserPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class CreateAdminUser(CreateAPIView):

    # Allow authenticate users to hit this endpoint
    permission_classes = (IsAuthenticated, )
    serializer_class = AdminUserSerializer

    def post(self, request):
        #restore those native datatypes into a dictionary of validated data.
        serializers = self.serializer_class(data=request.data)
        #checks if the data is as per serializer fields otherwise throws an exception.
        serializers.is_valid(raise_exception=True)
        serializers.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success' : 'True',
            'statuc code' : status_code,
            'message' : 'User registered successfully'
        }

        return Response(response, status=status_code)


class AdminLogin(RetrieveUpdateDestroyAPIView):

    permission_classes = (AllowAny, )
    serializer_class = AdminLoginSerializer


    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status_code' : status.HTTP_200_OK,
            'firstname' : serializer.data['first_name'],
            'lastname' : serializer.data['last_name'],
            'email' : serializer.data['email'],
            'token' : serializer.data['token'],
        }

        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

class UserListView(ListAPIView):

    permission_classes=(IsAuthenticated, )

    queryset = Admin.objects.all()
    serializer_class = AdminUserSerializer
