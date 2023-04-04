from rest_framework import routers
from api import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'houses', views.HouseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
