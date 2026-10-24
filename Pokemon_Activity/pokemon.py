import requests
response1 = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
response2= requests.get("https://pokeapi.co/api/v2/pokemon/charizard")
response = requests.get("https://pokeapi.co/api/v2/pokemon/blastoise")
response = requests.get("https://pokeapi.co/api/v2/pokemon/kakuna ")
response = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")

pokemons = response1
pokemon = pokemons.json()

response1 = {
    "name" : pokemon.get("name"),
    "height" : pokemon.get("height"),
    "weight" : pokemon.get("weight")
}

response2 = {
    "name" : pokemon.get("name"),
    "height" : pokemon.get("height"),
    "weight" : pokemon.get("weight")
}

print(response1["name"])
print(response1["height"])
print(response1["weight"])





















