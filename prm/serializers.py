from rest_framework import serializers
from prm.models import Project, User, Task


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userName',)
class UserSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'email', 'userRole']
class UserSettingPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', )



