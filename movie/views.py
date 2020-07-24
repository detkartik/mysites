
from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import MovieSerializer, MovieMiniSerializer, RatingSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from .models import Movie, Rating
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all().order_by('id')
    serializer_class = MovieSerializer

    @action(detail=True, methods=['post'])
    def rate_movie(self, request, pk=None):
        response = {'message': 'its working'}
        return Response(response, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MovieSerializer(instance)
        return Response(serializer.data)


class RatingViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Rating.objects.all().order_by('id')
    serializer_class = RatingSerializer

    def update(self, request, *args, **kwargs):
        response = {'message': 'You cannot update the ratings like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You cannot create the ratings like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
