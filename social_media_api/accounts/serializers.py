from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import CustomUser

# Serializer for the CustomUser model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']


# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    # Add a password confirmation field
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
        }

    # Overriding the create method to include user and token creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=password
        )

        # Create an authentication token for the user
        Token.objects.create(user=user)
        
        return user
