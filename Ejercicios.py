#Practica 2 de Comunicaciones Digitales curso 20-21
#Miguel Antunes García

import argparse
import os
import platform
from Repeticion import *
from Paridad import *


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-n","--number",help ="Ejemplo que se quiere ejecutar y su explicación (1.Codigos de repeticion 2.Codigos de paridad 3.Codigos bloque)",type =int)
    args = parser.parse_args()

    syst = platform.system()

    print(syst)

    if(platform.system() == 'Windows'):
        os.system('cls')
    elif(platform.system() == 'Linux'):
        os.system('clear')

    #Generamos un mensaje de nbits para utilizar en los ejercicios
    n_bits = 100000
    ones = random.randint(0,n_bits)
    zeroes = n_bits-ones
    data = [0]*zeroes + [1]*ones
    data = random.sample(data,n_bits)

    if(args.number == 1): #Códigos de repetición
        print('Ejercicios de codigos de repeticion:\n')
        
        rep_number = 3
        pe = 0.02
        pri_n = 4

        print('Primeros {} bits a codificar y enviar:'.format(pri_n))
        print(data[0:pri_n])

        codigoTx = CodificadorRepeticion(data,rep_number)
        
        print('Codigo con repeticion (primeros {} valores repetidos):'.format(pri_n))
        print(codigoTx[0:(pri_n*rep_number)])
        
        codigoRx = Canal(codigoTx,pe)

        print('Primeros datos recibidos del canal:')
        print(codigoRx[0:(pri_n*rep_number)])
        
        bits = DecodificadorRepeticion(codigoRx,rep_number)
        
        print('Primeros {} bits decodificados tras pasar por el canal:'.format(pri_n))
        print(bits[0:pri_n])
        
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
        t_err = (3*pow(pe,2))-(2*pow(pe,3))
        print('El error teórico para el caso de n = 3 es de:')
        print(t_err)
        print('\n')
        print('Si el número de bits es suficientemente elevado ambas probabilidades deberían ser similares')
        
       
    elif(args.number == 2):
        print('Ejercicios de codigos de paridad:\n')
        
        n = 3
        pe = 0.02
        pri_n = 5

        print('Primeros {} mensajes a codificar y enviar:'.format(pri_n))
        print(data[0:((n-1)*pri_n)])
       

        codigoTx = CodificadorParidad(data,n)
        print('Codigo conparidad par:')
        print(codigoTx[0:(n*pri_n)])
        

        codigoRx = Canal(codigoTx,pe)
        print('Datos recibidos del canal:')
        print(codigoRx[0:(n*pri_n)])
      

        bitsRx = DecodificadorParidad(codigoRx,n)
        print('Primeros bits decodificados tras pasar por el canal:')
        print(bitsRx[0:((n-1)*pri_n)])
      
        print('Numero de bits detectados como erroneos (si ha habido algún error detectado se marcan todos como erroneos) :')
        err = 0
        for i in range(n_bits):
            if(bitsRx[i]==-1):
                err+=1
        print("{}\n".format(err))

        err = n*(n-1)*0.5*pow(pe,2)

        print("La probabilidad de que no se haya detectado ningun error (para n = 3 implica que haya 2 bits eroneos) es de:\n{:1.8}".format(err))
        
        


    elif(args.number == 3):
        print('3')





if __name__ == "__main__":
    main()