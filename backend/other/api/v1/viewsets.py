from rest_framework import authentication
from other.models import Foreign_Asset1, Foreign_Asset2
from .serializers import Foreign_Asset1Serializer, Foreign_Asset2Serializer
from rest_framework import viewsets


class Foreign_Asset1ViewSet(viewsets.ModelViewSet):
    serializer_class = Foreign_Asset1Serializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Foreign_Asset1.objects.all()


class Foreign_Asset2ViewSet(viewsets.ModelViewSet):
    serializer_class = Foreign_Asset2Serializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Foreign_Asset2.objects.all()
