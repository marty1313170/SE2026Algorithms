import requests

# API LINK
base_url = "https://pokeapi.co/api/v2/"

def ask_user_for_pokemon_wanted():
    pokemon_wanted = input("What pokemon would you like to learn about")

    return pokemon_wanted



def get_pokemon_info(pokemon_wanted):
    url = f"{base_url}/pokemon/{pokemon_wanted}"
    response = requests.get(url)

    if response.status_code == 200:
        return pokemon_data
    else:
        print(f"Failed to retreive{response.pokemon_data}")
    return

def print_pokemon_info():
    print(f"Name: {pokemon_info['name'].capitalize()}")
    return

ask_user_for_pokemon_wanted()
get_pokemon_info(pokemon_wanted)
print_pokemon_info()

    


    
 
