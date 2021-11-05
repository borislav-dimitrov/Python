from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user.models import profile
from user.models import profile
from user.models import profile
from user.models import profile
from user.models import profile


class profileS(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = ['picture', 'birthDate']


class userSerializer(serializers.HyperlinkedModelSerializer):
    profile = profileS()

    class Meta:
        model = User
        fields = ['url', 'profile', 'is_staff', 'is_active', 'id', 'first_name', 'last_name', 'email', 'last_login',
                  'date_joined',
                  'username']

    def update(self, instance, validated_data):
        profile = instance.profile
        user = User.objects.filter(username=validated_data['username']).first()

        instance.first_name = validated_data.get('first_name', user.first_name)
        instance.last_name = validated_data.get('last_name', user.last_name)
        instance.email = validated_data.get('email', user.email)
        instance.is_active = validated_data.get('is_active', user.is_active)
        instance.is_staff = validated_data.get('is_staff', user.is_staff)
        instance.last_login = validated_data.get('last_login', user.last_login)
        instance.save()

        if validated_data.get('profile'):
            profile.picture = validated_data.get('profile').get('picture', user.profile.picture)
            profile.birthDate = validated_data.get('profile').get('birthDate', user.profile.birthDate)
            profile.save()

        # Slow down method so users can see the loading bar
        for i in range(150000):
            print("hello")

        return instance


class userRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            '',
            validated_data['password']
        )

        users = []
        for i in range(100):
            users.append(validated_data['username']+i)

        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class userProfileSerializer(serializers.ModelSerializer):
    user = userSerializer()
    birthdays = serializers.CharField(source='birthDate')

    class Meta:
        model = profile
        fields = ['user', 'picture', 'birthDate', 'birthdays']


class customTokenObtainPairViewSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        data['user_id'] = str(self.user.pk)

        return data
