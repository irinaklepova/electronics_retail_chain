from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from trading_network.models import Product, Contact, Provider
from trading_network.permissions import IsActiveStaff
from trading_network.serializers import ContactSerializer, ProviderSerializer, ProductSerializer
from trading_network.services import CountryFilter


class ProductViewSet(viewsets.ModelViewSet):
    """Контроллер CRUD для продукта"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActiveStaff,)


class ContactViewSet(viewsets.ModelViewSet):
    """Контроллер CRUD для контакта"""

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsActiveStaff,)


class ProviderViewSet(viewsets.ModelViewSet):
    """Контроллер CRUD для поставщика"""

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CountryFilter
    permission_classes = (IsActiveStaff,)
