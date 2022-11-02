from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =StudentExtra
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model =TeacherExtra
        fields = "__all__"

