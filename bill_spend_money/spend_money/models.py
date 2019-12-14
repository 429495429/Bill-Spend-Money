from django.db import models

# Create your models here.
class Products(models.Model):
	product_name = models.CharField(max_length=200)
	product_image = models.CharField(max_length=200)
	product_price = models.IntegerField()

	def __str__(self):
		return f"{self.product_name} ${product_price} "
