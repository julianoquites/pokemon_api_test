import requests

def get_pokemon():

  print("***Hey! Welcome to Pokemon API Test!***\n\n")

  pokemon = input("Please, enter a pokemon name: ").lower()

  request_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'

  pokemon_data = requests.get(request_url).json()

  pokemon_img = f'{pokemon_data["sprites"]["other"]["official-artwork"]["front_default"]}'

  print(f'Name: {pokemon_data["forms"][0]["name"].capitalize()}')
  print(f'Type: {pokemon_data["types"][0]["type"]["name"]}')
  print(f'Index: {pokemon_data["id"]}')
 
get_pokemon()
