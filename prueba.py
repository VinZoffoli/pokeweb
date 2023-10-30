def filtrar_pokemon_salud_alta(pokemon_lista):
    # Utilizamos la función de orden superior 'filter' para filtrar los Pokémon cuya salud sea mayor o igual a 70
    pokemon_filtrados = filter(lambda pokemon: pokemon['salud'] >= 70, pokemon_lista)
    # Convertimos el resultado a una lista para obtener los Pokémon que cumplen con el criterio
    return list(pokemon_filtrados)
# Lista de Pokémon con sus características
pokemones = [
    {'nombre': 'Pikachu', 'tipo': 'Eléctrico', 'salud': 60},
    {'nombre': 'Charizard', 'tipo': 'Fuego', 'salud': 78},
    {'nombre': 'Mewtwo', 'tipo': 'Psíquico', 'salud': 90}
]

# Llamamos a la función para filtrar los Pokémon con salud alta
pokemon_salud_alta = filtrar_pokemon_salud_alta(pokemones)

# Imprimimos los resultados
print(pokemon_salud_alta)
