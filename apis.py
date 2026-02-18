import requests


base_url= "https://pokeapi.co/api/v2/"


def fetch_pokemon(name):
    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url)
    
    if response.status_code == 200:
        data=response.json()
        return data
    else:
        print("Error occured")    
    
    
pokemon_name="typhlosion"
pokemon_info=fetch_pokemon(pokemon_name)



if fetch_pokemon:
    print(f"Name: {pokemon_info["name"]}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")
    