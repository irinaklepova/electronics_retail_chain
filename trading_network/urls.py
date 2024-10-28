from rest_framework.routers import DefaultRouter

from trading_network.apps import TradingNetworkConfig
from trading_network.views import ContactViewSet, ProductViewSet, ProviderViewSet

app_name = TradingNetworkConfig.name

provider_router = DefaultRouter()
provider_router.register(r"provider", ProviderViewSet, basename="provider")

product_router = DefaultRouter()
product_router.register(r"product", ProductViewSet, basename="product")

contact_router = DefaultRouter()
contact_router.register(r"contact", ContactViewSet, basename="contact")


urlpatterns = [] + provider_router.urls + product_router.urls + contact_router.urls
