from django.urls import path, include
from rest_framework import routers

from missions.views import MissionViewSet

router = routers.DefaultRouter()
router.register('', MissionViewSet)

urlpatterns = [path('', include(router.urls))]

app_name = 'missions'
