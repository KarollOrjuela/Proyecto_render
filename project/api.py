from .models import Project
from rest_framework import viewsets,permissions
from .serializers import ProjectSerializer

# vista principal donde se renderiza los datos dentro del modelo
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class = ProjectSerializer # serializador
