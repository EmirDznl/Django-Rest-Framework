
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from Kitaplar.api.serializers import KitapSerializer, YorumSerializer
from Kitaplar.models import Kitap, Yorum
from rest_framework import permissions
from Kitaplar.api.permissions import IsAdminUserOrReadOnly, IsYorumSahibiOrReadOnly
from rest_framework.exceptions import ValidationError
from Kitaplar.api.pagination import SmallPagination, LargePagination



class KitapListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer
    pagination_class = SmallPagination


class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer
    pagination_class = SmallPagination


class YorumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [IsYorumSahibiOrReadOnly]
    pagination_class = SmallPagination


class YorumCreateAPIView(generics.CreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = SmallPagination
    def perform_create(self, serializer):
        #path('kitaplar/<int:kitap_pk>/yorum_yap/', api_views.YorumCreateAPIView.as_view(), name='kitap-yorumla'),
        kitap_pk = self.kwargs.get('kitap_pk')
        
        
        kitap = get_object_or_404(Kitap, pk=kitap_pk)
        yorum_sahibi = self.request.user
        
        yorumlar = Yorum.objects.filter(kitap=kitap, yorum_sahibi=yorum_sahibi)
        if yorumlar.exists():
            raise ValidationError('Bir kitaba bir yorum')
        
        serializer.save(kitap=kitap, yorum_sahibi=yorum_sahibi)