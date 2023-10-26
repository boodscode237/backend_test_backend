from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import MaterialViewSet, UserViewSet, NanoparticleViewSet, SynthesisViewSet, NovaViewSet, ArticleViewSet

router = DefaultRouter()
router.register(r'materials', MaterialViewSet)
router.register(r'users', UserViewSet)
router.register(r'nanoparticles', NanoparticleViewSet)
router.register(r'syntheses', SynthesisViewSet)
router.register(r'novas', NovaViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
