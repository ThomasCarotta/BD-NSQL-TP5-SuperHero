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
        "name": "Iron Man",
        "real_name": "Tony Stark",
        "debut_year": 1936,
        "house": "Marvel",
        "biography": " Genio multimillonario que construye armaduras tecnológicas para combatir el crimen.",
        "equipment": "Armadura Mark",
        "images": ["https://imgs.search.brave.com/VDU9WwqvTE8SR17YTG1OmLDALl80HKsdiuq9NwPIogA/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAyMy8w/OS8wMi8xOC8yNC9h/aS1nZW5lcmF0ZWQt/ODIyOTM5M182NDAu/cG5n"]
    }
]

for h in heroes:
    if not SuperHero.objects(name=h["name"]).first():
        SuperHero(**h).save()
        print(f"Insertado: {h['name']}")
    else:
        print(f"Ya existe: {h['name']}")
