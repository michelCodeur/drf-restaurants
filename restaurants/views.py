from rest_framework import generics

from restaurants.permissions import IsOwnerOrReadOnly  # <- import generics
from .models import Restaurant, Review  # <- don't forget your models
from .serializers import RestaurantSerializer, ReviewSerializer  # <- or serializers
from rest_framework import permissions
from restaurants.permissions import IsOwnerOrReadOnly


class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # overwrite create method
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # overwrite create method
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]
