import requests
from colorama import init

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
def load_pokemon():
    print("Loading Pokemon..........")
    #
    request = requests.get('https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json')
    #
    pokedex = []
    #
    for item in request.json():
        pokemon = Pokemon(item["id"], item["name"]["english"], item["type"])
        pokedex.append(pokemon)

    return pokedex

def main():
    init()

    pokedex = load_pokemon()









main()