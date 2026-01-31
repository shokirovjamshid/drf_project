

from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.serializers import ModelSerializer

from apps.models import CartItem, Cart, Product, Category, Seller, District, Region


class SellerModelSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class SubCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance:Category):
        re = super().to_representation(instance)
        re['sub_categories'] = SubCategoryModelSerializer(instance.children,many=True).data
        return re


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartItemModelSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = 'quantity','product'

    def validate(self, attrs):
        cart_item_quantity = attrs.get('quantity')
        product = attrs.get('product')
        if cart_item_quantity > product.quantity:
            raise ValidationError('Omborda mahsulot yetarli emas')
        return attrs

    def create(self, validated_data):
        request = self.context['request']
        cart, created = Cart.objects.get_or_create(user=request.user)
        validated_data['cart'] = cart
        return super().create(validated_data)


class DistrictModelSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = 'name',


class RegionModelSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
