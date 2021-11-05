from rest_framework import serializers

from car.models import Brand, Model, Rating, Comment


class brandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'image', 'url', 'name', 'year_established']


class modelListSerializer(serializers.ModelSerializer):
    brand = brandSerializer()
    brand1 = brandSerializer()
    brand2 = brandSerializer()

    class Meta:
        model = Model
        fields = ['id', 'description', 'image', 'name', 'brand', 'brand2',
                  'brand1']


class modelCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['id', 'description', 'image', 'name', 'brand']


class ratingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'rating']


class commentListSerializer(serializers.ModelSerializer):
    rating = ratingSerializer(many=True)
    # Will the owner have usename or full name
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'owner', 'comment', 'rating']

class commentCRUDSerializerOfCommentWithOwnerReadOnly_field(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'owner', 'comment', 'rating']
