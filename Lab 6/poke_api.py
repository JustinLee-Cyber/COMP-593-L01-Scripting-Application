'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # TODO: Clean the Pokemon name parameter

    pokemon_name = str(pokemon_name).strip().lower()

    #check if pokemon name is an empty string

    if pokemon_name == '':
        print('Error: Pokemon does not exist')
        return

    # TODO: Build a clean URL and use it to send a GET request

    url = POKE_API_URL + pokemon_name

    #Send a GET request for pokemon info

    print(f'Getting Information for {pokemon_name}....', end='')

    request_pok = requests.get(url)

# TODO: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    #Check if the request is successful 

    if request_pok.status_code == requests.codes.ok:
        print('Successful')
        #return information
        return request_pok.json()
    else:
        print('Unsuccessful')
        print(f'Respond code: {request_pok.status_code}')
        print(f'Reason: {request_pok.reason}')

    # TODO: If the GET request failed, print the error reason and return None





    return

if __name__ == '__main__':
    main()