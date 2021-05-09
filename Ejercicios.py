#Practica 2 de Comunicaciones Digitales curso 20-21
#Miguel Antunes García

import argparse
import os
import platform
from Repeticion import *
from Paridad import *
from Bloque import *

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-n","--number",help ="Ejemplo que se quiere ejecutar y su explicación (1.Codigos de repeticion 2.Codigos de paridad 3.Codigos bloque)",type =int)
    args = parser.parse_args()

    syst = platform.system()

    if(platform.system() == 'Windows'):
        os.system('cls')
    elif(platform.system() == 'Linux'):
        os.system('clear')

    #Generamos un mensaje de nbits para utilizar en los ejercicios 
    n_bits = 10000

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

        print('Ejercicios de codigos Hamming:\n')
        (g,h) = MatricesHamming(3)
        print("Matriz generadora: \n{}\nMatriz de comprobacion: \n{}\n".format(g,h))

        codigoTx = CodificadorHamming(data,g)
        codigoRx = Canal(codigoTx,0.02)
        bits = DecodificadorHamming(codigoRx,h)

        print("Primeros bits a codificar: {}".format(data[0:8]))
        print("Primeros bits decodificados en el destino: {}".format(bits[0:8]))
        print("CodeTx (primeras 2 palabras):{}".format(codigoTx[0:14]))
        print("CodeRx (primeras 2 palabras):{}".format(codigoRx[0:14]))
        
        
        err = 0
        for i in range(len(codigoRx)):
            if(codigoRx[i]!=codigoTx[i]):
                err+=1
        print('Numero de bits erroneos por Canal (diferencia entre bits a la entrada y salida del canal, es decir, ya codificados):{}'.format(err))

        err = 0
        for i in range(n_bits):
            if(data[i]!=bits[i]):
                err+=1
        print('Numero de bits erroneos tras decodificar por Hamming (diferencia entre los bits originales y los obtenidos tras la decodificacion):{}'.format(err))
        print('La probabilidad de error obtenida es de {}\n\nPara comprobar el funcionamiento se va a transmitir el siguiente texto:'.format(err/n_bits))

        
        text = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor"
        print(text)

        data = []
        for c in text:
            for bit in ("{0:08b}".format(ord(c))):
                data.append(int(bit))
                
        
        codigoTx = CodificadorHamming(data,g)
        codigoRx = Canal(codigoTx,0.02)
        bits = DecodificadorHamming(codigoRx,h)

        text_corregido = ""
        for i in range(0,len(bits),8):
            bits_slice = bits[i:(i+8)]
            val = "{}{}{}{}{}{}{}{}".format(bits_slice[0],bits_slice[1],bits_slice[2],bits_slice[3],bits_slice[4],bits_slice[5],bits_slice[6],bits_slice[7])
            text_corregido += chr(int(val,2))
        
        print("Texto con errores corregidos:\n{}".format(text_corregido))

        bits = []
        text_raw = ""
        for i in range(0,len(codigoRx),7):
            bits_slice = codigoRx[i:(i+7)]
            bits+= bits_slice[0:4]
        

        for i in range(0,len(bits),8):
            bits_slice = bits[i:(i+8)]
            val = "{}{}{}{}{}{}{}{}".format(bits_slice[0],bits_slice[1],bits_slice[2],bits_slice[3],bits_slice[4],bits_slice[5],bits_slice[6],bits_slice[7])
            text_raw += chr(int(val,2))
        
        print("Texto sin corrección:\n{}\n\nSe puede comprobar que se corrigen la mayoría de los errores, aunque algunos no se han detectado o no se han podido corregir".format(text_raw))
        
        


if __name__ == "__main__":
    main()