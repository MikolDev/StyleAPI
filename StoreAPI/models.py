from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField()

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title
