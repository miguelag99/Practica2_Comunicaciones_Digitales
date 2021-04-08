import math

def CodificadorParidad(bits,n):
    #A partir de un array de 1xN bits se genera un array con la codificacion con paridad PAR

    codigo = []

    #Debemos tener cuidado en caso de que el numero de bits del mensaje no sea divisible entre (n-1) (no debería darse ya que el mensaje original debe poder dibidirse en palabras de ese tamaño)

    if((len(bits)%(n-1)) == 0):

        n_cod = int(len(bits)/(n-1))

        for i in range(n_cod):
            
            part = bits[i*(n-1):(i+1)*(n-1)]

            if((sum(part)%2) == 0):
                part.extend([0])
            else:
                part.extend([1])

            codigo.extend(part)

    else: #No debería darse el caso, pero lo tenemos en cuenta por si ocurre algún error

        n_cod = int(math.floor(len(bits)/(n-1)))

        for i in range(n_cod):
            
            part = bits[i*(n-1):(i+1)*(n-1)]

            if((sum(part)%2) == 0):
                part.extend([0])
            else:
                part.extend([1])

            codigo.extend(part)       
        
        part = bits[(n_cod)*(n-1):]

        if((sum(part)%2) == 0):
            part.extend([0])
        else:
            part.extend([1])

        codigo.extend(part)

    return codigo


def DecodificadorParidad(codigo,n):
    #A partir de un mensaje codificado con paridad PAR detectamos los errores

    n_cod = int(len(codigo)/n)
    bits = []

    for i in range(n_cod):

        part = codigo[i*n:(i+1)*n]
        

        if ((sum(part)%2)!=0):
            part = [-1]*(len(part)-1)
        else:
            part = part[0:(len(part)-1)]
        bits.extend(part)
        

    return bits


        



