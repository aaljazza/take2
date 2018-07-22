from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from app.models import Restaurant
from .serializers import RestaurantListSerializer, RestaurantDetailSerializer, RestaurantCreateUpdateSerializer
from django.http import JsonResponse

# Create your views here.
# Django lets us do Model Based Views!

class RestaurantListView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class=RestaurantListSerializer

# Below is how to do the same thing but in Function View!
#def article_list_view(request):
#	queryset = Restaurant.objects.all()
#	json_data = RestaurantListSerializer(queryset, many=True).data
#	return JsonResponse(json_data, safe=False)

class RestaurantDetailView(RetrieveAPIView):
	queryset = Restaurant.objects.all()
	serializer_class=RestaurantDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'

# Below is how to do the same thing but in Function View!
#def restaurant_detail_view(request, restaurant_id):
#	restaurant = Restaurant.objects.get(id=restaurant_id)
#	json_data = RestaurantDetailSerializer(restaurant).data
#	return JsonResponse(json_data, safe=False)

class RestaurantUpdateView(RetrieveUpdateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class=RestaurantCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'

class RestaurantDeleteView(DestroyAPIView):
	queryset = Restaurant.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'

class RestaurantCreateView(CreateAPIView):
	serializer_class=RestaurantCreateUpdateSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
