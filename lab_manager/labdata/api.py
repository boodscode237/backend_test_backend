from rest_framework import viewsets, permissions
from .models import Material, User, Nanoparticle, Synthesis, Nova, Article
from .serializers import MaterialSerializer, UserSerializer, NanoparticleSerializer, SynthesisSerializer, \
    NovaSerializer, ArticleSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MaterialSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class NanoparticleViewSet(viewsets.ModelViewSet):
    queryset = Nanoparticle.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NanoparticleSerializer


class SynthesisViewSet(viewsets.ModelViewSet):
    queryset = Synthesis.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SynthesisSerializer


class NovaViewSet(viewsets.ModelViewSet):
    queryset = Nova.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NovaSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
