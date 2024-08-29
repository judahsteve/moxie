from django.urls import path, include
from rest_framework import routers
from medspa.views import MedspaViewSet

router = routers.DefaultRouter()
router.register(r'medspas', MedspaViewSet, basename='medspas')

urlpatterns = [
    path('', include(router.urls)),
]