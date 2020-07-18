import pokebase as pb


def isValid(nombre):
    if len(nombre) <= 8:
        for i in range(len(nombre)):
            if(not ((nombre[i] >= 'A' and nombre[i] <= 'Z') or (nombre[i] >= 'a' and nombre[i] <= 'z')) ):
                return 0
        return 1
    else:
        return 0

principal=input("ingresa tu nombre ")
while not isValid(principal):
        print('El nombre debe contener solo letras y ser menor a 8 caracteres')
        principal=input("ingresa el nombre ")


rival=input("ingresa el nombre del peruanito ")
while not isValid(rival):
        print('El nombre debe contener solo letras y ser menor a 8 caracteres')
        rival=input("ingresa el nombre ")


print("tu nombre es ",principal)
print("el nombre del rival es ",rival)


print("hola bienvenido al mundo de los pokemons ")

team=[]

print("elige tu primer pokemon")
starter=int(input("1-Bulbasaur\n2-Charmander\n3-Squirtle\n"))
while starter < 1 and starter > 3:
    print("elegi bien capo")
    starter=input("1-Bulbasaur\n2-Charmander\n3-Squirtle\n")
if starter==2:
    team.append('charmander')
elif starter == 3:
    team.append('squirtle')
elif starter == 1:
    team.append('bulbasaur')


pokebaseStats = {
    'hp': 0,
    'att' : 1,
    'def' : 2,
    'sp-att' : 3,
    'sp-def' : 4,
    'sp' : 5 
}


myFirstPokemon = pb.pokemon(team[0])
hp=myFirstPokemon.stats[pokebaseStats.get('hp')].stat.name
attack=myFirstPokemon.stats[pokebaseStats.get('att')].stat.name
defense=myFirstPokemon.stats[pokebaseStats.get('def')].stat.name
specialattack=myFirstPokemon.stats[pokebaseStats.get('sp-att')].stat.name
specialdefense=myFirstPokemon.stats[pokebaseStats.get('sp-def')].stat.name
speed=myFirstPokemon.stats[pokebaseStats.get('sp')].stat.name

Nivel = 5
myPokemonStats{
    'HP': ,
    'Attack' :,
    'Defense' : ,
    'Special-Attack' : ,
    'Special-Defense' : ,
    'Speed' :  
}
PS: 10 + { Nivel / 100 x [ (hp x 2) ] } + Nivel

for i in range(1,6):
     myPokemonStats[i] = ( 5 + { Nivel / 100 x [ (myFirstPokemon.stats[i] x 2) ] )
