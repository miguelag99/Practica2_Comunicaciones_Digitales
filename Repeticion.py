import random

def CodificadorRepeticion(bits,n):
    #A partir de un array de 1xN bits se genera un array de 1x(nN)

    codigo = []

    for bit in bits:
        codigo.extend([bit]*n)

    return codigo


def DecodificadorRepeticion(codigo,n):
    #A partir de un array codificado de 1x(nN) se decodifican los bits originales

    n_bits = int(len(codigo)/n)
    bits = []

    for i in range(n_bits):
        data = codigo[(n*i):(n*(i+1))]

        if((sum(data)/n)>0.5):
            bit = 1
        elif((sum(data)/n)<0.5):
            bit = 0

        bits.append(bit)

    return bits


def Canal(codigoTx,p):
    #Simulamos los errores introducidos por un canal

    codigoRx = []
    prob = [0]*int((1-p)*1000)+[1]*int(p*1000)  #Generamos la probabilidad utilizando una lista

    for bit in codigoTx:
        if(random.choice(prob)):
            codigoRx.append(bit^1)
        else:
            codigoRx.append(bit)

    return codigoRx

