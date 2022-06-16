
from rest_framework import serializers
from users.models import Profile
from projects.models import Project, Rating
from django.contrib.auth.models import User



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'work_title',
            'image',
            'bio',
            'github',
            'linkedin',
            'twitter'
        ]

        # read_only_fields = ('user',)
        # depth = 1


class UserSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer(many=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'profile']

        read_only_fields = ('profile',)
        depth = 1



class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = [
            'design',
            'usability',
            'content'
        ]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


