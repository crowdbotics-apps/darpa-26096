from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Foreign_Asset1ViewSet, Foreign_Asset2ViewSet

router = DefaultRouter()
router.register("foreign_asset1", Foreign_Asset1ViewSet)
router.register("foreign_asset2", Foreign_Asset2ViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
