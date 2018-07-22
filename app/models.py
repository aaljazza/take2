from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
	name = models.CharField(max_length=120)
	slogan = models.CharField(max_length=240)
	created_on=models.DateTimeField(auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True)
	owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	logo = models.ImageField()

	def __str__(self):
		return self.name

class Like(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)

class FavoriteRestaurant(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)