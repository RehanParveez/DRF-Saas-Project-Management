from teams.views import TeamViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'team', TeamViewset, basename='team')

urlpatterns = [
    path('', include(router.urls)),
]
