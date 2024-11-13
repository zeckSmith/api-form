
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, FormulaireClientViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'formulaires', FormulaireClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
