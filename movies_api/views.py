from rest_framework import generics
from .serializer import MovieSerializer
from .models import Movies
from .permissions import IsOwnerOrReadOnly


class MovieList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


# Create your views here.
