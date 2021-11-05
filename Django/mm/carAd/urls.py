from django.urls import path
from carAd.views import *

urlpatterns = [
    path('type/', typeListCreate.as_view(), name='type-list'),
    path('type/<int:pk>/', typeCRUD.as_view(), name='type-detail'),
    path('specification/', specificationList.as_view(), name='specification-list'),
    path('specification/create', specificationCreate.as_view(), name='specification-create'),
    path('specification/<int:pk>/', specificationRUD.as_view(), name='specification-detail'),
    path('post/', carPostList.as_view(), name='carpost-list'),
    path('post/<int:pk>/', carPostRUD.as_view(), name='carpost-detail'),
    path('post/create/', carPostCreate.as_view(), name='carpost-create'),
    path('post/picture/', postPictureList.as_view(), name='postpicture-list'),
    path('post/picture/<int:pk>/', postPictureRUD.as_view(), name='postpicture-detail'),
    path('post/picture/create/', postPictureCreate.as_view(), name='postpicture-create'),
    path('post/picture/default', postPictureDefault.as_view())
]
