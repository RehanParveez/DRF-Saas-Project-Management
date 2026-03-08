from tasks.views import TagViewset, TaskViewset, SubTaskViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'tag', TagViewset, basename='tag')
router.register(r'tasks', TaskViewset, basename='task')
router.register(r'subtask', SubTaskViewset, basename='subtask')

urlpatterns = [
    path('', include(router.urls)),
]