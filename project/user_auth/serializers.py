from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        def create(self, clean_data):
            user_obj = UserModel.objects.create_user(email=clean_data['email'])
            user_obj.username = clean_data['username']
            user_obj.save()

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        user = UserModel.objects.get(email=clean_data['email'])

        if not user:
            raise ValidationError('User not found')

        if not check_password(clean_data['password'], user.password):
            raise ValidationError('Authentication details are incorrect.')

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["username", "first_name", "last_name", "email"]