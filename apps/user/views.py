from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import serializers, viewsets
from rest_framework.permissions import DjangoModelPermissions
from apps.user.models import UserProfile
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from collections import OrderedDict
from django.utils.datastructures import MultiValueDictKeyError


class LargeResultsSetPagination(LimitOffsetPagination):
    limit_query_param = 'length'
    offset_query_param = 'start'
    max_limit = 100

    def get_paginated_response(self, data):
        try:
            draw = self.request.query_params.get('draw')
        except MultiValueDictKeyError:
            draw = 1

        return Response(OrderedDict([
            ('recordsTotal', self.count),
            ('recordsFiltered', self.count),
            ('draw', draw),
            ('data', data)
        ]))


class BaseViewSet(viewsets.ModelViewSet):
    filter_backends = (SearchFilter, OrderingFilter)
    permission_classes = [DjangoModelPermissions]


# Create your views here.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ['user_permissions']

    def create(self, validated_data):
        # user = UserProfile.objects.create_user(**validated_data)
        # user.set_password()
        validated_data.update({'password': make_password(validated_data.get('password'))})
        print('OK')
        user = UserProfile.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class UserViewSet(viewsets.ModelViewSet):
    filter_backends = (SearchFilter, OrderingFilter)
    # permission_classes = [DjangoModelPermissions]
    serializer_class = UserSerializer
    pagination_class = LargeResultsSetPagination
    # pagination_class = LimitOffsetPagination
    model = UserProfile
    queryset = UserProfile.objects.all()
    search_fields = ('first_name', 'last_name')
    ordering_fields = ('first_name', 'last_name')
