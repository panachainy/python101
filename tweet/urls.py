from django.urls import path

from . import views

urlpatterns = [
    path('tweet/', views.tweet_list),
    path('tweet/<int:pk>/', views.tweet_detail),
]