from notifications.views import ActivityViewset, NotificationViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'activity', ActivityViewset, basename='activity')
router.register(r'notification', NotificationViewset, basename='notification')

urlpatterns = [
    path('', include(router.urls)),
]