import numpy as np
import math

def MatricesHamming(q):

    n = pow(2,q)-1
    k = pow(2,q)-1-q

    h = np.zeros((q,k))
    g = np.zeros((k,q))

    print(h)
    I = np.eye(q,q)
    
    values = np.arange(pow(2,q))
    values = np.delete(values,0)

    for value in values:
        binary = np.zeros((q,1))
        binary_str = format(value,"b").zfill(q)

        

        if (math.ceil(math.log2(value))!=math.log2(value)):
            for i in range(q):
                binary[i,0] = int(binary_str[i])

            if(h.shape == ((q,k))):
                h = binary
            else:
                h = np.concatenate((h,binary),axis = 1)
            
    g = np.transpose(h)
    g = np.concatenate((np.eye(k),g),axis = 1)
    h = np.concatenate((h,I),axis = 1)    
    return (g,h)


def CodificadorHamming(bits,g):
    (k,n) = g.shape
    q = n - k

    codigo = np.array([])
    max_msg = int(len(bits)/k)

    for i in range(max_msg):

        bits_slice = bits[i*k:(i+1)*k]

        tr_bit = np.mod(np.dot(bits_slice,g),2)
        
        codigo = np.append(codigo,tr_bit)
    
    return codigo
    
    #La suma es una xor y el producto es una or


def DecodificadorHamming(codigo,h):
    (q,n) = h.shape
    k = n - q

    max_msg = int(len(codigo)/n)
    bits = np.array([])

    err_vect = np.eye(n)
    print(err_vect)

    

    for i in range(max_msg):

        code_slice = codigo[i*n:(i+1)*n]

        syndrome = np.mod(np.dot(code_slice,np.transpose(h)),2)
        print(syndrome)
        print(h.shape)








    