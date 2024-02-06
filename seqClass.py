#!/usr/bin/env python

#IMPORTAMOS ALUGNOS MÓDULOS
import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence") #OBIGATORIO PONER -s o --seq
parser.add_argument("-m", "--motif", type=str, required = False, help = "Motif") # NO ES OBLIGATORIO poner -m o --motif

# COMPROBAMOS SI SE HAN AÑADIDO ARGUMENTOS (-s o -seq) EN LA LÍNEA DE COMANDOS. 
if len(sys.argv) == 1:
    parser.print_help() # te imprime ayuda del programa
    sys.exit(1) # se sale del programa

args = parser.parse_args() # analiza los argumentos proporcionados en la línea de comandos

args.seq = args.seq.upper()                 # Note we just added this line. lo converte a mayusculas
if re.search('^[ACGTU]+$', args.seq): # comprueba si la secuencia de entrada es DNA o RNA
    if re.search('T', args.seq): #si secuencia contiene T, es DNA
        print ('The sequence is DNA')
    elif re.search('U', args.seq): # si secuencia contiene U, es RNA
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA') # si secuencia no contiene ni T ni U (pero sí A,C,G)
else:
    print ('The secuence is neither DNA nor RNA')#!/usr/bin/env python # si la secuencia contiene cualquier otro caracter

if args.motif: #si se ha proporcionado un motif
	args.motif = args.motif.upper()
	print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
	if re.search(args.motif, args.seq): #busca el motif dentro de la secuencia
		print("MOTIF FOUND") #esta es la modificación que he hecho en el fix

	else:
		print("MOTIF NOT FOUND") #este es el del fix
