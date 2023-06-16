from django.urls import (
    include,
    path
)
from rest_framework_nested import routers
from .views import PropostaViewSet

router = routers.SimpleRouter()

router.register("proposta", PropostaViewSet, basename="proposta")

urlpatterns = [
    path('', include(router.urls)),
]
