#Practica 2 de Comunicaciones Digitales curso 20-21
#Miguel Antunes García

import argparse
from Repeticion import *



def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-n","--number",help ="Ejemplo que se quiere ejecutar y su explicación (1.Codigos de repeticion 2.Codigos de paridad 3.Codigos bloque)",type =int)
    args = parser.parse_args()

    if(args.number == 1): #Códigos de repetición
        print('Ejemplo de codigos de repeticion:\n')
        
        rep_number = 3
        pe = 0.02
        n_bits = 100000

        ones = random.randint(0,n_bits)
        zeroes = n_bits-ones
        data = [0]*zeroes + [1]*ones
        data = random.sample(data,n_bits)

        print('Primeros 10 bits a codificar y enviar:\n')
        print(data[0:(10*rep_number)])
        #print(data)
        print('\n')

        codigoTx = CodificadorRepeticion(data,rep_number)
        
        print('Codigo con repeticion (primeros 10 valores repetidos):\n')
        #print(codigoTx)
        print(codigoTx[0:(10*rep_number)])
        print('\n')
        
        codigoRx = Canal(codigoTx,pe)

        print('Primeros datos recibidos del canal (se corresponderían con los 10 primeros bits repetidos):\n')
        #print(codigoRx)
        print(codigoRx[0:(10*rep_number)])
        print('\n')
        
        bits = DecodificadorRepeticion(codigoRx,rep_number)
        
        print('Primeros 10 bits decodificados tras pasar por el canal:\n')
        #print(bits)
        print(bits[0:(10*rep_number)])
        print('\n')
        
        if(bits == data):
            print('Decodificacion correcta (los bits recibidos son los enviados) \n\n')
        else:
            print('Los errores introducidos por el canal no ha permitido detectar y corregir la información\n\n')
        

        print('Numero de bits erroneos:')
        err = 0
        for i in range(n_bits):
            if(data[i]!=bits[i]):
                err+=1
            
        print(err)
        err = (err/n_bits)
        print('probabilidad de error en este caso:')
        print(err)
        print('\n')
        t_err = (3*pow(pe,2))-(2*pow(pe,3))
        print('El error teórico para el caso de n = 3 es de:')
        print(t_err)
        print('\n')
        
       
    elif(args.number == 2):
        print('2')
    elif(args.number == 3):
        print('3')





if __name__ == "__main__":
    main()