from django.apps import AppConfig


class VirmarketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'VirMarket'

    def ready(self) -> None:
        import VirMarket.signals
