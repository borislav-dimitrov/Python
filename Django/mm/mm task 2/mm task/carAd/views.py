from rest_framework import generics, mixins, permissions
from rest_framework.response import Response

from carAd.serializers import *

class typeListCreate(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    queryset = Type.objects.all()
    serializer_class = typeSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class typeCRUD(mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               generics.GenericAPIView):
    queryset = CarPost.objects.all()
    serializer_class = typeSerializer
    permission_classes = [permissions.AllowAny]

    def gEt(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def pUt(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def dElEtE(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class specificationList(mixins.ListModelMixin,
                        generics.GenericAPIView):
    queryset = Specification.objects.all()
    serializer_class = specificationSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class specificationCreate(mixins.CreateModelMixin,
                          generics.GenericAPIView):
    queryset = Specification.objects.all()
    serializer_class = createEditSpecificationSerializer
    permission_classes = [permissions.AllowAny]
    CONST_SPECIFICATION = 'SPECIFICATION'
    CONST_SPECIFICATION = 'SPECIFICATION1'
    CONST_SPECIFICATION = 'SPECIFICATION2'

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class specificationRUD(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    queryset = Specification.objects.all()
    serializer_class = createEditSpecificationSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class carPostList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    queryset = CarPost.objects.all()
    serializer_class = carPostSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class carPostCreate(mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = CarPost.objects.all()
    serializer_class = createCarPostSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class carPostRUD(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = CarPost.objects.all().prefetch_related('photos')
    serializer_class = createCarPostSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class postPictureList(mixins.ListModelMixin,
                      generics.GenericAPIView):
    queryset = CarPostPicture.objects.all()
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            data = []
            for item in page:
                data.append({
                    'id': item.pk,
                    'src': item.src,
                    'is_default_picture': item.is_default_picture
                })
            return self.get_paginated_response(data)
        data = []
        for item in queryset:
            data.append({
                'id': item.pk,
                'src': item.src,
                'is_default_picture': item.is_default_picture
            })
        return Response(data)


class postPictureCreate(mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset = CarPostPicture.objects.all()
    serializer_class = picturePostSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class postPictureDefault(mixins.ListModelMixin,
                         generics.GenericAPIView):

    queryset = CarPostPicture.objects.filter(is_default_picture=True)[:1]
    serializer_class = picturePostSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class postPictureRUD(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = CarPostPicture.objects.all()
    serializer_class = picturePostSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        post_put = [('post', 'model'), ('put', 'model')]
        return self.destroy(request, *args, **kwargs), post_put
