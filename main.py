from settings import *
import sys

chr1, rule1 = "F", "F-G+F+G-F"
chr2, rule2 = "G", "GG"
base = "F"
nbGens= 7


def apply_rules (base): #
    return ''.join([rule1 if char == chr1 else 
                    rule2 if char == chr2 else char for char in base]) #on aurait aussi pu faire une concaténation avec chaine += rule1 etc

def get_instructions (nbGens, base) :
    #global base #on fait appel à la variable base globale
    for gen in range(nbGens):
        base = apply_rules(base) #la valeur de base est remplacée par la valeur de chaine
    return base

instructions = get_instructions(nbGens, base)
canva = Canva()
draw = canva.draw

try :
    for char in instructions :
        if char == chr1 or char ==chr2 :
            draw.forward(step)
        elif char == '+' :
            draw.right(angle)
        elif char == '-' :
            draw.left(angle)
    canva.close()
except :
    sys.exit()


