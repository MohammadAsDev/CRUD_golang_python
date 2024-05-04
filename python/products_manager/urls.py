from django.urls import path

from .views import * 

urlpatterns = [
    path("<int:pk>/" , view=ProductDetails.as_view(), name="product_details"),
    path("" , view=ProductsList.as_view(), name="products_list"),
]
