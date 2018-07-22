from rest_framework import serializers
from app.models import Restaurant

class RestaurantListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ['id', 'name', 'logo', 'owner','created_on','updated_on']


class RestaurantDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = '__all__'


class RestaurantCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ['name','slogan','logo']


