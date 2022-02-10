from rest_framework import serializers
from .models import Restaurant, Review

# Reviews


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    # Link the restaurant primary key on the review table to the restaurant that it belongs to on the restaurant table
    restaurant_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(),
        source='restaurant'
    )

    # how to populate the owner field on review data
    owner = serializers.ReadOnlyField(source='owner.username')

    restaurant = serializers.HyperlinkedRelatedField(
        view_name='restaurant_detail', read_only=True)

    class Meta:
        model = Review
        fields = ('title', 'restaurant', 'body',
                  'owner', 'restaurant_id', 'restaurant')


# Restaurants
class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    # reviews = serializers.HyperlinkedRelatedField(
    #     view_name='review_detail', many=True, read_only=True)

    # if you want to just return all the JSON reviews in a list for a given restaurant
    reviews = ReviewSerializer(many=True, read_only=True)

    # how to populate the owner field on restaurant data
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'reviews', 'cuisine', 'owner')
