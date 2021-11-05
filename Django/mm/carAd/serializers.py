from rest_framework import serializers
from car.serializers import modelListSerializer
from car.serializers import brandSerializer
from car.serializers import modelCRUDSerializer
from car.serializers import ratingSerializer
from car.serializers import commentListSerializer
from car.serializers import commentCRUDSerializerOfCommentWithOwnerReadOnly_field
from carAd.models import *
class typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']
class createEditSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ['id', 'the_name_of_the_specificSpecification', 'type']
class specificationSerializer(serializers.Serializer):
    type = typeSerializer()
    id = serializers.IntegerField()
    the_name_of_the_specificSpecification = serializers.CharField()
class picturePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPostPicture
        fields = ['id', 'src', 'is_default_picture']
class carPostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    model = modelListSerializer()
    price = serializers.IntegerField()
    published = serializers.DateTimeField()
    description = serializers.CharField()
    phone_number = serializers.CharField()
    owner = serializers.ReadOnlyField(source='owner.username')
    photos = picturePostSerializer(many=True)
    specifications = specificationSerializer(many=True)

    class Meta:
        model = CarPost
        fields = ['id', 'model', 'price', 'published', 'description', 'phone_number', 'owner', 'photos',
                  'specifications']
class createCarPostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CarPost
        fields = ['model', 'price', 'published', 'description', 'phone_number', 'owner', 'photos', 'specifications']
