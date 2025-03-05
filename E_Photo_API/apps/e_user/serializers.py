from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.SlugRelatedField(
        queryset=Group.objects.all(),
        slug_field='name',
        many=True,
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

