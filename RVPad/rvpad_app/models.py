

from django.db import models
from login_registration_app.models import User


class RestaurantManager(models.Manager):
    def restaurant_validator(self, postData):
        errors = {}

        if len(postData['name']) < 2:
            errors['name'] = 'Name should be at least 2 characters'

        if len(postData['description']) < 2:
            errors['description'] = 'Description should be at least 10 characters'

        return errors


class ReviewManager(models.Manager):
    def review_validator(self, postData):
        errors = {}

        if len(postData['name']) < 2:
            errors['name'] = 'Name should be at least 2 characters'

        if len(postData['description']) < 2:
            errors['description'] = 'Description should be at least 10 characters'

        return errors


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='images/', default='/static/imgs/no_image.png')
    posted_by = models.ForeignKey(
        User, related_name="restaurants", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RestaurantManager()

    def __str__(self):
        return f"<Restaurant object: {self.name}>"


class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField()
    posted_by = models.ForeignKey(
        User, related_name="reviews", on_delete=models.CASCADE)
    reviewed_restaurant = models.ForeignKey(
        Restaurant, related_name="reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()

    def __str__(self):
        return f"<Review object: {self.rating}>"
