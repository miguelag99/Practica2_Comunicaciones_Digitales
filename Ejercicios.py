#Practica 2 de Comunicaciones Digitales
import argparse
from Repeticion import *



def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-n","--number",help ="Ejemplo que se quiere ejecutar (1.Codigos de repeticion 2.Codigos de paridad 3.Codigos bloque)",type =int)
    args = parser.parse_args()

    if(args.number == 1): #Códigos de repetición
        print('Ejemplo de codigos de repeticion:\n')

        rep_number = 3
        pe = 0.02
        n_bits = 10000

        ones = random.randint(0,n_bits)
        zeroes = n_bits-ones
        data = [0]*zeroes + [1]*ones
        data = random.sample(data,n_bits)

        codigoTx = CodificadorRepeticion(data,rep_number)
        '''
        print('Codigo con repeticion:\n')
        print(codigoTx)
        print('\n')
        '''
        codigoRx = Canal(codigoTx,pe)
        '''
        print('Codigo recibido del canal:\n')
        print(codigoRx)
        print('\n')
        '''
        bits = DecodificadorRepeticion(codigoRx,rep_number)
        '''
        print('Codigo decodificado:\n')
        print(bits)
        print('\n')
        '''
        if(bits == data):
            print('Decodificacion correcta')

    elif(args.number == 2):
        print('2')
    elif(args.number == 3):
        print('3')





if __name__ == "__main__":
    main()