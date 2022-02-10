
from django.db import models

# Create your models here.


class Restaurant(models.Model):
    # name: A char field
    name = models.CharField(max_length=100)
    # cuisine: A char field
    cuisine = models.CharField(max_length=100)
    owner = models.ForeignKey(
        'users.User', related_name='restaurants', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Review(models.Model):
    # title: A char field
    title = models.CharField(max_length=100)
    # restaurant: A foreign key for the related restaurant
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='reviews')
    # body: A text field
    body = models.TextField()
    owner = models.ForeignKey(
        'users.User', related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
