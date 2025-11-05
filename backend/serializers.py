from django.contrib.auth.models import User
from rest_framework import serializers
from .models import TaskModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ["id", "taskOwner", "description", "created_at", "status"]
        extra_kwargs = {
            "taskOwner": {"read_only": True}, 
            "created_at": {"read_only": True},
            }
        read_only_fields = ["status, id"]
