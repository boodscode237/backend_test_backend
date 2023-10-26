from rest_framework import serializers
from .models import Material, User, Nanoparticle, Synthesis, Nova, Article


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'password']


class NanoparticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nanoparticle
        fields = '__all__'


class SynthesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synthesis
        fields = '__all__'


class NovaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nova
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
