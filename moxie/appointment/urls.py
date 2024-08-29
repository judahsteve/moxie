from django.urls import path, include
from rest_framework import routers
from appointment.views import AppointmentViewSet

router = routers.DefaultRouter()
router.register(r'appointments', AppointmentViewSet, basename='appointments')

urlpatterns = [
    path('appointments/status/<str:status>/', AppointmentViewSet.as_view({"get": "get_by_status"})),
    path('appointments/start-date/<str:start_date>/', AppointmentViewSet.as_view({"get": "get_by_start_date"})),
    path('', include(router.urls)),
    
]