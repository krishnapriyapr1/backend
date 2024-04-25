from rest_framework import serializers
from events.models import Event
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        read_only_fields=["id"]
        fields=["id","username","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
