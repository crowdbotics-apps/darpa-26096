from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CustomTextViewSet,
    DoD_Asset1ViewSet,
    DoD_Asset2ViewSet,
    DoD_Asset3ViewSet,
    HomePageViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("dod_asset3", DoD_Asset3ViewSet)
router.register("dod_asset2", DoD_Asset2ViewSet)
router.register("dod_asset1", DoD_Asset1ViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
