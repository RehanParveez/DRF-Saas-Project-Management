from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'phone', 'profession', 'dob', 'is_active', 'is_staff' 'created_at']
        
    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
            phone=validated_data.get('phone'),
            profession=validated_data.get('profession'),
            dob=validated_data.get('dob'),
            dob=validated_data.get('is_active'),
            dob=validated_data.get('is_staff'),
            created_at=validated_data.get('created_at'),  
        )
        return user