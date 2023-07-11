from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = (permissions.IsAuthenticated,) # Is Authenticated para autenticaciones
    serializer_class = ProjectSerializer
