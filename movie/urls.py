from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'movie', views.MovieViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'rating', views.RatingViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
