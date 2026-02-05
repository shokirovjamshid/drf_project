from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.views import CartItemCreateAPIView, ProductCreateAPIView, CategoryCreateAPIView, SellerCreateAPIView, \
    DistrictListAPIView, RegionListAPIView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('cart', CartItemCreateAPIView.as_view()),
    path('product', ProductCreateAPIView.as_view()),
    path('category', CategoryCreateAPIView.as_view()),
    path('celler', SellerCreateAPIView.as_view()),
    path('districts', DistrictListAPIView.as_view()),
    path('regions', RegionListAPIView.as_view())
]
