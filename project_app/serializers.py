from rest_framework import serializers

from .models import Project, TODO
from users.models import User
from users.serializers import UserModelSerializer


class ProjectModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class TODOModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TODO
        fields = '__all__'
