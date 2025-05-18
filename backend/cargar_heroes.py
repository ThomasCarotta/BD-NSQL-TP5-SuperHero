import mongoengine
from APISuperHero.models import SuperHero

# Conectar manualmente a MongoDB
mongoengine.connect(
    db='superheroesdb',
    host='localhost',
    alias='default'
)

# Lista de superhéroes de ejemplo
heroes = [
    {
        "name": "Spider-Man",
        "real_name": "Peter Parker",
        "debut_year": 1962,
        "house": "Marvel",
        "biography": "Fue mordido por una araña radioactiva...",
        "equipment": "Lanzatelarañas",
        "images": ["https://i.pinimg.com/originals/f0/69/cf/f069cf1a2635c6c840775ccbd6131ddb.jpg"]
    },
    {
        "name": "Batman",
        "real_name": "Bruce Wayne",
        "debut_year": 1939,
        "house": "DC",
        "biography": "Millonario que combate el crimen en Gotham.",
        "equipment": "Baticinturón, Batimóvil",
        "images": ["https://static.wikia.nocookie.net/batman/images/c/cc/344.jpg/revision/latest?cb=20150524150900&path-prefix=es", "https://i.pinimg.com/originals/d7/3f/5b/d73f5b35fd44114e29b4d08af74b0949.jpg"]
    },
]

# Insertar héroes
for h in heroes:
    if not SuperHero.objects(name=h["name"]).first():  # evitar duplicados
        SuperHero(**h).save()
        print(f"Insertado: {h['name']}")
    else:
        print(f"Ya existe: {h['name']}")
