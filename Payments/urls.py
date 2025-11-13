from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, PaymentViewSet, ExpenseViewSet

router = DefaultRouter()
router.register(r'vendors', VendorViewSet, basename='vendor')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'expenses', ExpenseViewSet, basename='expense')

urlpatterns = router.urls
