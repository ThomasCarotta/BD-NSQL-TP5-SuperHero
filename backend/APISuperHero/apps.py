# backend/APISuperHero/apps.py

from django.apps import AppConfig
import mongoengine

class ApisuperheroConfig(AppConfig):
    name = 'APISuperHero'

    def ready(self):
        mongoengine.connect(
            db='superheroesdb',
            host='localhost',  # o 'mongodb://localhost:27017/superheroesdb'
            alias='default'
        )
