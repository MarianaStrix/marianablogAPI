from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets

from .permissions import IsMyAccountOrReadOnly
from .serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsMyAccountOrReadOnly, )
