from rest_framework import generics, mixins, viewsets
from books.models import Book
from .serializers import bookSerializer

class BookAPIView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    # We don’t want to book model in Ember and the Book model in Django to clash. Setting the resource_name here nips that issue in the bud.
    resource_name = 'books'
    serializer_class = bookSerializer

