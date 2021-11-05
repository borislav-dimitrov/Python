from rest_framework import permissions, generics, mixins, views
from rest_framework.response import Response

from car.serializers import *


from user.serializers import userSerializer


class brandList(views.APIView):
    @staticmethod
    def get(request):
        models = ['1', '23', 'X5']
        brands = []
        for brand in Brand.objects.all():
            brands.append({
                'id': brand.pk,
                'image': brand.image,
                'name': brand.name,
                'year_established': brand.year_established
            })
        return Response(data=brands)


class brandDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Brand.objects.all()
    serializer_class = brandSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        get_request = 'get  ----  request'
        return self.retrieve(request, *args, **kwargs), get_request

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class modelList(mixins.ListModelMixin,
                generics.GenericAPIView):
    queryset = Model.objects.all()
    serializer_class = modelListSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class modelCRUD(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.CreateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = Model.objects.all().select_related('brand')
    serializer_class = userSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        post_put = [('post', 'model'), ('put', 'model')]
        return self.update(request, *args, **kwargs), post_put

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ratingList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Rating.objects.all()
    serializer_class = ratingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ratingRUD(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = Rating.objects.all()
    serializer_class = ratingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class commentList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = commentListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class commentCreate(mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = commentCRUDSerializerOfCommentWithOwnerReadOnly_field
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class commentRUD(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = commentCRUDSerializerOfCommentWithOwnerReadOnly_field
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
