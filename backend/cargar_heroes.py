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
        "images": ["https://imgs.search.brave.com/9HlBs1WZqHKA-07slt6i_INfWEnPq1omKnHeC1Zaxm8/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAyMi8x/MC8xNi8wNy80Mi9z/dXBlcmhlcm8tNzUy/NDQ3MV82NDAucG5n",
                   "https://imgs.search.brave.com/msd3VnOZb0lJtFcYZex1PWvB8scRmnGhRmu_LrgErIk/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTcx/MTY1NjMxL3Bob3Rv/L25ldy15b3JrLW55/LWFjdG9yLWFuZHJl/dy1nYXJmaWVsZC1l/bnRlcnMtdGhlLXRo/ZS1hbWF6aW5nLXNw/aWRlcm1hbi0yLW1v/dmllLXNldC1pbi1t/YWRpc29uLmpwZz9z/PTYxMng2MTImdz0w/Jms9MjAmYz1VNUpH/Wk1mZ09lUEQ3VG90/YS01Yi1ZeGxuYXI1/akpMcU85OUFodzBO/TnpnPQ"]
    },
    {
        "name": "Iron Man",
        "real_name": "Tony Stark",
        "debut_year": 1936,
        "house": "Marvel",
        "biography": "Genio multimillonario que construye armaduras tecnológicas para combatir el crimen.",
        "equipment": "Armadura Mark",
        "images": ["https://imgs.search.brave.com/VDU9WwqvTE8SR17YTG1OmLDALl80HKsdiuq9NwPIogA/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAyMy8w/OS8wMi8xOC8yNC9h/aS1nZW5lcmF0ZWQt/ODIyOTM5M182NDAu/cG5n"]
    },
    {
        "name": "Thor Odinson",
        "real_name": "Thor Odinson",
        "debut_year": 1962,
        "house": "Marvel",
        "biography": "Dios nórdico del trueno, hijo de Odín, protector de la Tierra.",
        "equipment": "Mjolnir, Stormbreaker",
        "images": ["https://imgs.search.brave.com/XOwXdvUkehjVl_GHc9urPmGuRwp3Szf1gbczoPDtixo/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly90aHVt/YnMuZHJlYW1zdGlt/ZS5jb20vYi9sYXMt/dmVnYXMtbnYtdXNh/LW9jdC1jaHJpcy1o/ZW1zd29ydGgtYXMt/dGhvci1zY3JlZW4t/YXZlbmdlcnMtc3Rh/dGlvbi1jb21wbGV4/LWxhcy12ZWdhcy1j/aHJpcy1oZW1zd29y/dGgtYXMtdGhvci0x/MTM0Nzc5NDUuanBn"]
    },
    {
        "name": "Batman",
        "real_name": "Bruce Wayne",
        "debut_year": 1939,
        "house": "DC",
        "biography": " Detective multimillonario sin poderes, maestro del combate.",
        "equipment": "Batarangs, traje blindado, Batimóvil, gadgets variados",
        "images": ["https://imgs.search.brave.com/_AZBn9IX3l7vUMJvj4U61-NTkzG9A0KLzpXqUxPPFkY/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tLm1l/ZGlhLWFtYXpvbi5j/b20vaW1hZ2VzL0kv/NzFUS2RSanBJQkwu/anBn",
                   "https://imgs.search.brave.com/o9Nfb9WqKNgxmxveiYTrC6I-4gEeSjzrP-VD_UNAl2M/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzRhLzEx/LzBiLzRhMTEwYjQw/OGE2MDdjYThkYjgx/OTY4NjU1NTI4MDM2/LmpwZw"]
    },
    {
        "name": "Wonder Woman",
        "real_name": "Diana Prince",
        "debut_year": 1941,
        "house": "DC",
        "biography": "Amazona guerrera, hija de Zeus, defensora de la paz.",
        "equipment": "Brazaletes indestructibles, lazo de la verdad, espada y escudo.",
        "images": ["https://armchairjournal.com/wp-content/uploads/2020/08/a5-Shifat-Khan.jpg"]
    },
    {
        "name": "Superman",
        "real_name": "Clark Kent",
        "debut_year": 1938,
        "house": "DC",
        "biography": "Kryptoniano con superfuerza, vuelo y visión de calor.",
        "equipment": "Traje de Krypton, capa, ocasionalmente anillos de kryptonita.",
        "images": ["https://media.revistagq.com/photos/643ffd0043b7dde5906f2d7e/master/pass/904934.jpg"]
    },
]

for h in heroes:
    if not SuperHero.objects(name=h["name"]).first():
        SuperHero(**h).save()
        print(f"Insertado: {h['name']}")
    else:
        print(f"Ya existe: {h['name']}")
