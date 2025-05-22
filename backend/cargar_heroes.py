import mongoengine
import os
from APISuperHero.models import SuperHero

mongoengine.connect(
    db='superheroesdb',
    host=os.environ.get('MONGO_HOST', 'localhost'),
    port=27017,
    alias='default'
)

heroes = [
    {
        "name": "Spider-Man",
        "real_name": "Peter Parker",
        "debut_year": 1962,
        "house": "Marvel",
        "biography": "Fue mordido por una araña radioactiva...",
        "equipment": "Lanzatelarañas",
        "images": ["https://i.imgur.com/SpiderMan1.jpg"]
    },
    {
        "name": "Batman",
        "real_name": "Bruce Wayne",
        "debut_year": 1939,
        "house": "DC",
        "biography": "Millonario que combate el crimen en Gotham.",
        "equipment": "Baticinturón, Batimóvil",
        "images": [
            "https://i.imgur.com/Batman1.jpg",
            "https://i.imgur.com/Batman2.jpg"
        ]
    }
]

for h in heroes:
    if not SuperHero.objects(name=h["name"]).first():
        SuperHero(**h).save()
        print(f"Insertado: {h['name']}")
    else:
        print(f"Ya existe: {h['name']}")
