import requests
import random


def game():

    pokemons = ["pikachu", "charizard", "blastoise", "kakuna", "charmander"]

    name = random.choice(pokemons)

    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + name)

    if response.status_code != 200:
      print("Couldn't find that pokemon.", response.status_code)
      exit()

    pokemon = response.json()

    info = {
    "name" : pokemon.get("name"),
    "height" : pokemon.get("height"),
    "weight" : pokemon.get("weight"),
    "ability" : pokemon["abilities"][0]["ability"]["name"]
    }

    print("\nWho's that pokemon? \n")
    print("Height: ", info["height"])
    print("Weight: ", info["weight"])
    print("Abitlity: ", info["ability"])

    for attempts in range(3):
        guess = input("\nYour guess: ").strip().lower()

        if guess == info["name"]:
            print("Correct! It's " + info["name"] + "! You win! \n") 
            break
        else: 
            print("Wrong! Attempts left: ", 2 - attempts)
    else:
        print("\nYou lose! The Pokemon was " + info["name"] + ".")

while True:
    game()

    choice = input("Do you want to play again? ")

    if choice.lower() != "yes":
        break

