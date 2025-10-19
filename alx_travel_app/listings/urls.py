from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet, InitializePaymentAPIView, VerifyPaymentAPIView, ChapaCallbackView

router = DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'bookings', BookingViewSet, basename='booking')

app_name = "payments"

urlpatterns = [
    path('', include(router.urls)),
    path("chapa/init/", InitializePaymentAPIView.as_view(), name="chapa_init"),
    path("chapa/verify/<str:tx_ref>/", VerifyPaymentAPIView.as_view(), name="chapa_verify"),
    path("chapa/callback/", ChapaCallbackView.as_view(), name="chapa_callback"),
    path("chapa/return/", ChapaCallbackView.as_view(), name="chapa_return"),  # return_url handler same as callback
]
