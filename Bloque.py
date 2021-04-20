import numpy as np
import math

def MatricesHamming(q):

    n = pow(2,q)-1
    k = pow(2,q)-1-q

    h = np.zeros((q,k))
    g = np.zeros((k,q))

    print(h)
    I = np.eye(q,q)
    #h = np.concatenate((h,I),axis = 1)

    values = np.arange(pow(2,q))
    values = np.delete(values,0)

    for value in values:
        binary = np.zeros((q,1))
        binary_str = format(value,"b").zfill(q)

        print("Valor:{} bin:{}".format(value,binary_str))
        
        print("{}={}".format(math.ceil(math.log2(5)),math.log2(5)))

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

    
               



    