from projects.views import ProjectViewset, BoardViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'project', ProjectViewset, basename='project')
router.register(r'board', BoardViewset, basename='board')

urlpatterns = [
    path('', include(router.urls)),
]