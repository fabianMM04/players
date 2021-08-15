from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from django.http.response import JsonResponse
from django.core.paginator import Paginator

import math

from .models import Player
from .serializers import PlayerSerializer


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        count = self.page.paginator.count 
        if self.request.method == 'GET':
                
            page = self.request.query_params.get('page')
            if page is None:
                page = "1"
        return JsonResponse({
            'Page': int(page),
            'totalPages': math.ceil(count/self.page_size),
            'Items': len(data),
            'totalItems': count,
            'Players': data
        })
        

class ApiPlayerListView(ListAPIView):
    serializer_class = PlayerSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        try:
            queryset = Player.objects.all()
            playerName= self.request.query_params.get('search')
            order = self.request.query_params.get('order')
            if playerName is not None:
                if (order is None) or (order == "asc") :
                    queryset = queryset.filter(name__istartswith=playerName).order_by('name')
                else: 
                    queryset = queryset.filter(name__istartswith=playerName).order_by('-name')
            return queryset
        except:
            JsonResponse({"message": "Fallo comuniquese con el administrador del sistema"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TeamPlayerList(viewsets.ViewSet):
    try:
        queryset = Player.objects.all()
    except:
            JsonResponse({"message": "Fallo comuniquese con el administrador del sistema"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        try:
            data = JSONParser().parse(request)
            queryset = self.queryset.filter(team__icontains=data['Name'])
            serial_query = PlayerSerializer(queryset, many=True)
            count = len(serial_query.data)
            p_size = Paginator(serial_query.data,10)
            page_num = data['Page']
            page = p_size.page(page_num)
            return JsonResponse({
                'Page': page_num,
                'totalPages': math.ceil(count/10),
                'Items': len(page.object_list),
                'totalItems': count,
                'Players': page.object_list
            })
        except:
            return JsonResponse({"message": "No se encontro campo (Name o Page) en el request"}, status=status.HTTP_400_BAD_REQUEST)


        