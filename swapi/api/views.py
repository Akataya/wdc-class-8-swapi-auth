import json

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.authentication import *
from rest_framework.permissions import *

from api.models import People, Planet
from api.serializers import PeopleModelSerializer, PlanetModelSerializer
from api.permissions import IsUsernameStartingWithA, IsEvenPeopleID


class PeopleModelViewSet(viewsets.ModelViewSet):

    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticated, IsUsernameStartingWithA, IsEvenPeopleID)
    serializer_class = PeopleModelSerializer
    queryset = People.objects.all()

    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [IsAuthenticated(), IsUsernameStartingWithA()]
    #     return [IsAuthenticated(), IsEvenPeopleID()]


class PlanetModelViewSet(viewsets.ModelViewSet):

    serializer_class = PlanetModelSerializer
    queryset = Planet.objects.all()
