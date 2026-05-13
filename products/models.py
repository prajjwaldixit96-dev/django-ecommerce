from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):

        return self.name


class Product(models.Model):

    title = models.CharField(max_length=200)

    price = models.IntegerField()

    description = models.TextField()

    image = models.ImageField(upload_to='products/')

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title
    

from django.contrib.auth.models import User


class Review(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.user.username
    
class Wishlist(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.user.username