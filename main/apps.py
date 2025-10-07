from django.apps import AppConfig


class MainConfig(AppConfig):
    # Keep BigAutoField for Django built-in models compatibility
    # Our custom Product model uses UUIDs explicitly
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
