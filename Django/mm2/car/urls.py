from django.urls import path
from car.views import *
urlpatterns = [
    path('brands/', brandList.as_view(), name='brand-list-one-two-three'),
    path('brands/<int:pk>/', brandDetail.as_view(), name="brand-detail-one-two-three"),
    path('models/', modelList.as_view(), name='model-list-one-two-three'),
    path('models/<int:pk>/', modelCRUD.as_view(), name="model-detail-one-two-three"),
    path('rating/', ratingList.as_view(), name="rating-list-one-two-three"),
    path('rating/<int:pk>/', ratingRUD.as_view(), name="rating-detail-one-two-three"),
    path('comment/', commentList.as_view(), name="comment-list-one-two-three"),
    path('comment/<int:pk>/', commentRUD.as_view(), name="comment-detail-one-two-three"),
    path('comment/create', commentCreate.as_view(), name="comment-create")
]
