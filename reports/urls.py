from reports.views import ReportViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'report', ReportViewset, basename='report')

urlpatterns = [
    path('', include(router.urls))
]
