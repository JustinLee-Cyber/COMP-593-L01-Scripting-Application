""" 
Description: 
  Creates a new PasteBin paste that contains a list of abilities 
  for a specified Pokemon

Usage:
  python pokemon_paste.py poke_name

Parameters:
  poke_name = Pokemon name
"""
import sys
import poke_api
import pastebin_api

def main():
    poke_name = get_pokemon_name()
    poke_info = poke_api.get_pokemon_info(poke_name)
    if poke_info is not None:
        paste_title, paste_body = get_paste_data(poke_info)
        paste_url = pastebin_api.post_new_paste(paste_title, paste_body, '1M')
        if paste_url:
            print(paste_url)
        else:
            exit

def get_pokemon_name():
    """Gets the name of the Pokemon specified as a command line parameter.
    Aborts script execution if no command line parameter was provided.

    Returns:
        str: Pokemon name
    """
    # TODO: Function body
    if len(sys.argv) - 1 == 1:
        PokName = sys.argv[1]
        return PokName
    else:
        print("Error: No name included in command prompt after calling script")
        exit()

def get_paste_data(pokemon_info):
    """Builds the title and body text for a PasteBin paste that lists a Pokemon's abilities.

    Args:
        pokemon_info (dict): Dictionary of Pokemon information

    Returns:
        (str, str): Title and body text for the PasteBin paste
    """    
    # TODO: Build the paste title
    
    #Create a string that holds the pokemon info name and add 's and Abilities
    create_title = pokemon_info['name'].capitalize() + "'s Abilities"
    #testing of creating title for paste
    #print(create_title)

    # TODO: Build the paste body text

    #Created for string to use
    body_text_created = ""
    #Create for loop range
    for i in range(len(pokemon_info['abilities'])): #Grabing the abilities and how many is inside for range loop
        if i < len(pokemon_info['abilities']) - 1: #if len is below max range - 1 keep using this and hit enter - new line
            body_text_created +="- " + pokemon_info['abilities'][i]['ability']['name'].capitalize() + "\n"
        else: # else if not below max, do the same, as in adding the abilities name but not new line
            body_text_created +="- " + pokemon_info['abilities'][i]['ability']['name'].capitalize()

    #Testing print of creating body text to be used    
    #print(body_text_created)
    return (create_title, body_text_created)

if __name__ == '__main__':
    main()