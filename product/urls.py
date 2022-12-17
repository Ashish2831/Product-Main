from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router1 = DefaultRouter()
router2 = DefaultRouter()
router3 = DefaultRouter()

router1.register('', views.ProductMainModelViewset, basename="ProductMainModelViewset")
router2.register('', views.ProductColourModelViewset, basename="ProductColourModelViewset")
router3.register('', views.ProductImageModelViewset, basename="ProductImageModelViewset")

urlpatterns = [
    path('image/', include(router3.urls)),
    path('colour/', include(router2.urls)),
    path('', include(router1.urls)),
]
