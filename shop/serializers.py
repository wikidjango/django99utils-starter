from rest_framework import serializers
from django.contrib.auth.models import User

from utils.serializers import *


# class UserSerializer(OptionalFieldsMixin, serializers.Serializer):
# 	username = serializers.CharField()
# 	email = serializers.EmailField()
# 	age = serializers.IntegerField(required=False)


# class UserSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = ["username", "email"]



# class PageSerializer(serializers.Serializer):
# 	page = serializers.IntegerField(default=1)
# 	page_size = serializers.IntegerField(default=20)