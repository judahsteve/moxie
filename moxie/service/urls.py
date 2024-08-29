from django.urls import path, include
from rest_framework import routers
from service.views import ServiceViewSet

router = routers.DefaultRouter()
router.register(r'services', ServiceViewSet, basename='services')

urlpatterns = [
    path('services/medspa/<int:medspa>/', ServiceViewSet.as_view({"get": "get_by_medspa"})),
    path('', include(router.urls)),
]