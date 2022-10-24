from rest_framework import serializers
from .models import BlogModel, Comment, Izoh


class BlogModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = [
            'title',
            'description',
            'image',
            'slug'
        ]


class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = "__all__"


class BlogModelDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'description'
        ]


class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['description']


class IzohSerializer(serializers.ModelSerializer):

    class Meta:
        model = Izoh
        fields = "__all__"