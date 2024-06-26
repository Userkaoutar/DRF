from django.contrib import admin
from django.urls import path,include
from django.urls import path
from .views import ItemList, ItemDetail, LocationDetail, LocationList

urlpatterns = [
    path('', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
]