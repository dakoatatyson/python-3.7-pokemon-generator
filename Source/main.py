import requests
from colorama import init, Fore, Style

import random

class Pokemon:
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type

    def GetID(self):
        return self.id

    def GetName(self):
        return self.name

    def GetType(self):
        return self.type[0]

    def __repr__(self):
        return ("ID: %s Name: %s Type: %s" % (self.id, self.name, self.GetType()))

#
def print_pokemon(pokemon):
    type_color = {
        "Bug": Style.BRIGHT + Fore.GREEN,
        "Dark": Style.BRIGHT + Fore.BLACK,
        "Dragon": Style.NORMAL + Fore.BLUE,
        "Electric": Style.BRIGHT + Fore.YELLOW,
        "Fairy": Style.BRIGHT + Fore.MAGENTA,
        "Fighting": Style.NORMAL + Fore.RED,
        "Fire": Style.BRIGHT + Fore.RED,
        "Flying": Style.BRIGHT + Fore.WHITE,
        "Ghost": Style.DIM + Fore.BLUE,
        "Grass": Style.NORMAL + Fore.GREEN,
        "Ground": Style.DIM + Fore.RED,
        "Ice": Style.BRIGHT + Fore.CYAN,
        "Normal": Style.NORMAL + Fore.WHITE,
        "Poison": Style.DIM + Fore.MAGENTA,
        "Psychic": Style.NORMAL + Fore.MAGENTA,
        "Rock": Style.DIM + Fore.YELLOW,
        "Steel": Style.DIM + Fore.WHITE,
        "Water": Style.BRIGHT + Fore.BLUE
    }

    print(type_color[pokemon.GetType()] + "Id: %s Name: %s Type: %s" % (
        pokemon.GetID(), 
        pokemon.GetName(), 
        pokemon.GetType()))

#
def print_party(party):
    print(Style.RESET_ALL + "Your generated party is!!!..........")
    for pokemon in party:
        print_pokemon(pokemon)

#
def generate_party(pokedex):
    print(Style.RESET_ALL + "Generating party..........")
    party = []

    #
    for i in range(6):
        random_id = random.randrange(0, len(pokedex) - 1)
        party_member = pokedex[random_id]
        party.append(party_member)

    return party

#
def load_pokemon():
    print(Style.RESET_ALL + "Loading Pokemon..........")
    pokedex = []

    request = requests.get('https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json')

    for item in request.json():
        pokemon = Pokemon(item["id"], item["name"]["english"], item["type"])
        pokedex.append(pokemon)

    return pokedex

def main():
    init()

    active = True
    while active:
        pokedex = load_pokemon()

        party = generate_party(pokedex)

        print_party(party)
        
        response = input(Style.RESET_ALL + "Press Y to generate a new team\nPress Any Key to Exit!")
        if(response != "Y"):
            active = False

main()