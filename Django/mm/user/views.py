from rest_framework import mixins, permissions, generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from user.models import profile
from user.serializers import userSerializer, userRegisterSerializer, customTokenObtainPairViewSerializer, \
    userProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend

class UserRUD(mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer
    permissions = [permissions.DjangoObjectPermissions]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ListUsers(mixins.ListModelMixin,
                generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer
    permissions = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['is_active', 'is_staff']

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

class AdminListUsers(mixins.ListModelMixin,
                generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer
    permissions = [permissions.AllowAny]


class CreateUser(mixins.CreateModelMixin,
                 generics.GenericAPIView,
                 User):
    queryset = User.objects.all()
    serializer_class = userRegisterSerializer
    permissions = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CustomTokenObtainPairView(TokenObtainPairView):
    # Used for custom token obtain pair view serializing
    serializer_class = customTokenObtainPairViewSerializer


class ListProfile(mixins.ListModelMixin,
                  generics.GenericAPIView):
    queryset = profile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProfileRUD(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = profile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):

        # Should delete method delete whole user of just profile model?
        return self.destroy(request, *args, **kwargs)
