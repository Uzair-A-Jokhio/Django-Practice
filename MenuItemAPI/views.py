from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from MenuItemAPI.models import MenuItem , Category
from MenuItemAPI.serializers import MenuItemSerializer, CategorySerializer
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated



@api_view(["GET", 'POST'])
def menu_items(request):
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data)


@api_view()
def single_item(request, id):
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)

@api_view()
@permission_classes([IsAuthenticated])
def some_secret(request):
    if request.user.groups.filter(name='manager').exists():
        return Response({"message" : "only manager can see this message"})
    else:
        return Response({'message':'Your are not authorized'}, 403)

class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['title']