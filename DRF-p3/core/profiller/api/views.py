from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiller.models import Profil, ProfilDurum
from profiller.api.serializers import ProfilSerializer, ProfilDurumSerializer, ProfilFotoSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet, ModelViewSet
from rest_framework import mixins
from profiller.api.permissions import KendiProfiliOrReadOnly, DurumSahibiOrReadOnly
from rest_framework.filters import SearchFilter



class ProfilViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer
    permission_classes = (IsAuthenticated, KendiProfiliOrReadOnly,) 
    filter_backends = [SearchFilter]
    search_fields = ['sehir']

class ProfilDurumViewSet(ModelViewSet):
    
    serializer_class = ProfilDurumSerializer
    permission_classes = [IsAuthenticated, DurumSahibiOrReadOnly]


    def get_queryset(self):
        queryset = ProfilDurum.objects.all() 
        username = self.request.query_params.get("username")  

        if username:
            queryset = queryset.filter(user_profil__user__username=username)
            return queryset
        return queryset
    def perform_create(self, serializer):
        user_profil = self.request.user.profil
        serializer.save(user_profil= user_profil)


class ProfilFotoUpdateView(generics.UpdateAPIView):
    serializer_class = ProfilFotoSerializer
    permission_classes = [IsAuthenticated,]

    def get_object(self):
        profil_nesnesi = self.request.user.profil
        return profil_nesnesi