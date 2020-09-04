from rest_framework import serializers
from .models import MtAdminUser
from .models import UserManager

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import AuthenticationFailed
#from .utils import Authentication_Failed_Exception



JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MtAdminUser
        fields = ['admin_id','first_name','last_name','username','password','date_created','date_modified','email','is_active','is_staff','is_superuser','role','ip_address','user_lang','lost_password_code','session_token','last_login','user_access','status','contact_number','inventory_role_id','inventory_enabled']

    def create(self, validated_data):
        user = MtAdminUser.objects.create_superuser(**validated_data)
        return user




class AdminLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    first_name = serializers.CharField(max_length=255, default="firstname")
    last_name = serializers.CharField(max_length=255, default="lastname")

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)

        if user is None:
            raise AuthenticationFailed()

        try:
            #user is passed as an payload
            payload = JWT_PAYLOAD_HANDLER(user)
            #token is generated if
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except MtAdminUser.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password doesnot exists'
            )
        return {
            'first_name' : user.first_name,
            'last_name' : user.last_name,
            'email' : user.email,
            'token' : jwt_token
        }
