from rest_framework import serializers
from .models import Project

# Serializador con los campos a mostrar y caracteristicas (como el campo de solo lectura)
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'Title', 'Description', 'Created_at')
        read_only_fields = ('created_at', )
