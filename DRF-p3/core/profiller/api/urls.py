from django.urls import path, include
from profiller.api.views import ProfilViewSet, ProfilDurumViewSet, ProfilFotoUpdateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'kullanici-profilleri', ProfilViewSet)
router.register(r'durum', ProfilDurumViewSet, basename="durum")


urlpatterns = [
    path('', include(router.urls)),
    path("profil_foto/", ProfilFotoUpdateView.as_view(), name="foto-update"),

]