from django.urls import path
from user.views import *

urlpatterns = [
    path('register/', CreateUser.as_view(), name='user-create'),
    path('users/', ListUsers.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRUD.as_view(), name='user-detail'),
    path('members/', ListProfile.as_view(), name='profile-list'),
    path('members/<int:pk>/', ProfileRUD.as_view(), name='profile-detail')
]
