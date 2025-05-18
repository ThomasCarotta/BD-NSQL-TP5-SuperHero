# backend/APISuperHero/models.py
from mongoengine import Document, StringField, IntField, ListField

class SuperHero(Document):
    name = StringField(required=True)
    real_name = StringField()
    debut_year = IntField()
    house = StringField(choices=["Marvel", "DC"])
    biography = StringField()
    equipment = StringField()
    images = ListField(StringField())  # URLs de imágenes

    meta = {'collection': 'superheroes'}
