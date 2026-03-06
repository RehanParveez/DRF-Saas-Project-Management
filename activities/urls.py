from activities.views import CommentViewset, FileViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'comment', CommentViewset, basename='comment')
router.register(r'file', FileViewset, basename='file')

urlpatterns = [
    path('', include(router.urls)),
]