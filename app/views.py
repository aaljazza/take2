from django.shortcuts import render, redirect
from .models import Restaurant, Like, FavoriteRestaurant
from .forms import RestaurantForm, SignupForm, SigninForm
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from django.http import JsonResponse
import requests
import json

# Create your views here.
def news(request):
	#This is CNN!
	response = requests.get("https://newsapi.org/v2/top-headlines?sources=cnn&apiKey=09f6b9840153479ab29b939814ca7a05")
	context = {
	"response": response.json()
	}
	return render(request, 'news.html', context)


def fav_list(request):
	my_list=[]
	fav_restaurants=FavoriteRestaurant.objects.filter(user=request.user)
	for res in fav_restaurants:
		my_list.append(res.restaurant)

	query = request.GET.get("q")
	if query:
		my_list=my_list.filter(
			Q(name__contains=query)|
			Q(slogan__contains=query)
			).distinct()

	context = {
		"my_list":my_list
	}
	return render(request, "favlist.html", context)

def rest_list(request):
	restaurants = Restaurant.objects.all()
	query = request.GET.get("q")
	if query:
		restaurants=restaurants.filter(
			Q(name__contains=query)|
			Q(slogan__contains=query)
			).distinct()

	my_list=[]
	if request.user.is_authenticated:
		fav_restaurants=FavoriteRestaurant.objects.filter(user=request.user)
		for res in fav_restaurants:
			my_list.append(res.restaurant)

	context = {
		"restaurants":restaurants,
		"my_list":my_list
	}
	return render(request, "list.html", context)

def rest_detail(request, restaurant_id):
	restaurant = Restaurant.objects.get(id=restaurant_id)
	liked = False
	if request.user.is_authenticated:
		if Like.objects.filter(restaurant=restaurant, user=request.user).exists():
			liked = False
		else:
			liked = True
	post_like_count = restaurant.like_set.all().count()

	context = {
		"restaurant":restaurant,
		"post_like_count":post_like_count,
		"liked":liked,
	}

	return render(request, "detail.html", context)

def rest_create(request):
	if request.user.is_anonymous:
			return redirect('signin')
	form = RestaurantForm()
	if request.method == "POST":
		form = RestaurantForm(request.POST, request.FILES)
		if form.is_valid():
			restaurant = form.save(commit=False)
			restaurant.owner = request.user
			restaurant.save()
			return redirect('list')
	context = {
		"form":form
	}

	return render(request, 'create.html', context)

def rest_update(request, restaurant_id):
	restaurant = Restaurant.objects.get(id=restaurant_id)
	if not (request.user.is_staff or request.user == restaurant.owner):
		return redirect('list')
	form = RestaurantForm(instance=restaurant)
	if request.method =="POST":
		form = RestaurantForm(request.POST, request.FILES, instance=restaurant)
		if form.is_valid():
			form.save()
			return redirect('list')
	context = {
		"restaurant":restaurant,
		"form":form
	}
	return render(request, 'update.html', context)



def signup(request):
	form = SignupForm()
	if request.method =='POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(user.password)
			user.save()
			login(request, user)
			return redirect('list')
	context = {
		"form":form
	}
	return render(request, 'signup.html', context)

def signin(request):
	form = SigninForm()
	if request.method =='POST':
		form = SigninForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			auth_user = authenticate(username=username, password=password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect('list')
	context = {
		"form":form
	}
	return render(request, 'signin.html', context)

def signout(request):
	logout(request)
	return redirect('signin')


def ajax_like(request, restaurant_id):
	restaurant = Restaurant.objects.get(id=restaurant_id)
	new_like, created = Like.objects.get_or_create(restaurant=restaurant, user=request.user)
	if created:
		action="like"
	else:
		action = "unlike"
		new_like.delete()

	post_like_count = restaurant.like_set.all().count()
	response = {
		"action":action,
		"post_like_count":post_like_count,
	}
	return JsonResponse(response, safe=False)


def restaurant_favorite(request, restaurant_id):
	restaurant=Restaurant.objects.get(id=restaurant_id)
	fav, created = FavoriteRestaurant.objects.get_or_create(restaurant=restaurant, user=request.user)
	if created:
		action="yay"
	else:
		action="nay"
		fav.delete()

	response = {
		"action":action
	}
	return JsonResponse(response, safe=False)
