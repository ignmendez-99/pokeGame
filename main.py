import pokebase as pb
import string as str
import re

#charmander = pb.pokemon('charmander')
#print(charmander.height)

def isValidName(nombre):
    regex = re.compile('^[a-zA-Z]{1,8}$', re.I)
    match = regex.match(nombre)
    return bool(match)

def isValid(nombre):
    if len(nombre) <= 8:
        for i in range(len(nombre)):
            if ((nombre[i] >= 'A' and nombre[i] <= 'Z') or (nombre[i] >= 'a' and nombre[i] <= 'z')):
                return 1
            else:
                return 0
    else:
        return 0
#aguante boquita 


def getName(nombre):
    nombre=input()
    while not isValid(nombre):
        print('El nombre debe contener solo letras y ser menor a 8 caracteres')
        nombre=input("¿Cual es su nombre?\n")
    rival=input("¿Como se llama el peruano?\n")
    while not isValid(rival):
        print('El nombre debe contener solo letras y ser menor a 8 caracteres')
        rival=input("¿Cual es su nombre?\n")
    

getNames()
def padre():
    print("¿Cual es su nombre?\n")
    nombrePeronajeppal = getName()

nombre=input("cual es tu nombre")
def valid(nombre)
principal=nombre
