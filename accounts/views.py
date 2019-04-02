from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework import permissions

from accounts.serializers import AccountSerializer
from accounts.permissions import IsMyAccountOrReadOnly


class AccountViewSet(viewsets.ModelViewSet):
    """
    dffg
    """
    queryset = get_user_model().objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsMyAccountOrReadOnly,)

