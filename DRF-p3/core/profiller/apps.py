from django.apps import AppConfig


class ProfillerConfig(AppConfig):
    name = 'profiller'

    def ready(self):
        import profiller.signals
