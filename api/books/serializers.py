from rest_framework import serializers

from sample_app.models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    published_year = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return Book.create(**validated_data)

    # class Meta:
    #     model = Book
    #     fields = ("id", "title", "author", "published_year")