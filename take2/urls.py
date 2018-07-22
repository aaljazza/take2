"""take2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf.urls.static import static
from django.conf import settings
from api.views import RestaurantListView, RestaurantDetailView, RestaurantUpdateView, RestaurantCreateView, RestaurantDeleteView #, restaurant_detail_view, article_list_view,

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants/list/',views.rest_list,name="list"),
    path('restaurants/detail/<int:restaurant_id>/', views.rest_detail, name="detail"),
    path('restaurants/create/', views.rest_create, name="create"),    
    path('restaurants/update/<int:restaurant_id>/', views.rest_update, name="update"),    
    path('signup/', views.signup, name="signup"),    
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),  
    path('ajax_like/<int:restaurant_id>/', views.ajax_like, name="like_button"),
    path('restaurants/<int:restaurant_id>/favorite/',views.restaurant_favorite ,name='restaurant-favorite'),
    path('restaurants/favlist/',views.fav_list,name="favlist"),
    path('accounts/', include('allauth.urls')),
    path('news/', views.news, name='news'),
    path('api/list/', RestaurantListView.as_view(), name='api-list'),
    #path('api/list2/', article_list_view, name='api-list2'),
    path('api/detail/<int:restaurant_id>/', RestaurantDetailView.as_view(), name='api-detail'),
    #path('api/detail2/<int:restaurant_id>/', restaurant_detail_view, name='api-detail2'),
    path('api/update/<int:restaurant_id>/', RestaurantUpdateView.as_view(), name='api-update'),
    path('api/delete/<int:restaurant_id>/', RestaurantDeleteView.as_view(), name='api-delete'),
    path('api/create/', RestaurantCreateView.as_view(), name='api-create'),

]
if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)