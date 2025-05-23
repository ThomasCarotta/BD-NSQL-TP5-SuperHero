from django.apps import AppConfig
import mongoengine

class ApisuperheroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'APISuperHero'

    def ready(self):
        # Evita múltiples conexiones con el mismo alias
        try:
            mongoengine.disconnect(alias='default')
        except mongoengine.connection.ConnectionFailure:
            pass

        mongoengine.connect(
            db='superheroesdb',
            host='mongo',  # usa el nombre del servicio del contenedor, NO 'localhost'
            alias='default'
        )
