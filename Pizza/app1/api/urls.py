from django.urls import path
from django.urls.conf import include
from . import views
from app1.api.views import Storslists
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('stors', Storslists, basename="stors")


urlpatterns = [
    path('list/', views.PizzaList.as_view(), name="pizza_list"),
    path('list/<int:pk>/', views.PizzaDetails.as_view(), name="pizza_details"),

    path('', include(router.urls)),
    # path('stors/', views.StorsList.as_view(), name="store_list"),
    # path('stors/<int:pk>/', views.StorsDetails.as_view(), name="store_details"),

    path('list/<int:pk>/review/', views.ReviewList.as_view(), name="review_list"),
    path('list/<int:pk>/review_create/', views.ReviewCreate.as_view(), name="review_create"),
    path('list/review/<int:pk>/', views.ReviewDetails.as_view(), name="review_details"),


    # path('list/', views.pizza_list, name="pizza_list"),
    # path('<int:pk>/', views.pizza_details, name="pizza_details"),
]