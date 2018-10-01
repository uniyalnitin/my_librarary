from rest_framework import serializers
from books.models import Book

class bookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = (
                'id',
                'url',
                'title',
                'author',
                'description',
            )
