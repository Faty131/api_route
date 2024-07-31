from django.urls import path
from .views import CalculateRouteView, GenerateMapUrlView

urlpatterns = [
    path('calculate-route/', CalculateRouteView.as_view(), name='calculate-route'),
    path('generate-map-url/', GenerateMapUrlView.as_view(), name='generate-map-url'),
]