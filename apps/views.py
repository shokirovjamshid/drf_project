
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.custom_permission import IsSellerUser
from apps.models import CartItem, Category, Product, Seller, District
from apps.serializers import CartItemModelSerializer, CategoryModelSerializer, ProductModelSerializer, \
    SellerModelSerializer, DistrictModelSerializer


class CategoryCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = IsAuthenticated,


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = IsAuthenticated,IsSellerUser


class CartItemCreateAPIView(CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemModelSerializer
    permission_classes = IsAuthenticated,

class SellerCreateAPIView(CreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerModelSerializer
    permission_classes = IsAuthenticated,


class DistrictListAPIView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictModelSerializer
    permission_classes = IsAuthenticated,
    filter_backends = DjangoFilterBackend,
    filterset_fields = 'region_id',



