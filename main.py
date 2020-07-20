import pokebase as pb
from Pokemon import Pokemon
from pokebaseConstants import pokebaseStats


def isValid(name):
    if len(name) <= 8:
        for i in range(len(name)):
            if not (('A' <= name[i] <= 'Z') or ('a' <= name[i] <= 'z')):
                return 0
        return 1
    else:
        return 0


principal = input("ingresa tu nombre ")
while not isValid(principal):
    print('El nombre debe contener solo letras y ser menor a 8 caracteres')
    principal = input("ingresa el nombre ")

rival = input("ingresa el nombre del peruanito ")
while not isValid(rival):
    print('El nombre debe contener solo letras y ser menor a 8 caracteres')
    rival = input("ingresa el nombre ")

print("tu nombre es ", principal)
print("el nombre del rival es ", rival)

print("hola bienvenido al mundo de los pokemons ")

print("elige tu primer pokemon")
starter = int(input("1-Bulbasaur\n2-Charmander\n3-Squirtle\n"))
while 1 > starter > 3:
    print("elegi bien capo")
    starter = input("1-Bulbasaur\n2-Charmander\n3-Squirtle\n")
if starter == 1:
    firstPokemonName = 'bulbasaur'
elif starter == 2:
    firstPokemonName = 'charmander'
elif starter == 3:
    firstPokemonName = 'squirtle'

myFirstPokemon = pb.pokemon(firstPokemonName)
print(myFirstPokemon)

baseHP = myFirstPokemon.stats[pokebaseStats.get('hp')].base_stat
baseAttack = myFirstPokemon.stats[pokebaseStats.get('att')].base_stat
baseDefense = myFirstPokemon.stats[pokebaseStats.get('def')].base_stat
baseSpecialAttack = myFirstPokemon.stats[pokebaseStats.get('sp-att')].base_stat
baseSpecialDefense = myFirstPokemon.stats[pokebaseStats.get('sp-def')].base_stat
baseSpeed = myFirstPokemon.stats[pokebaseStats.get('sp')].base_stat

# Instantiate our first Pokemon
firstPokemon = Pokemon(firstPokemonName, 5, baseHP, baseAttack, baseDefense,
                       baseSpecialAttack, baseSpecialDefense, baseSpeed)

team = [firstPokemon]
