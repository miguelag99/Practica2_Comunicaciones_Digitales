import numpy as np
import math

def MatricesHamming(q):

    n = pow(2,q)-1
    k = pow(2,q)-1-q

    h = np.zeros((q,k))
    g = np.zeros((k,q))

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
    
    codigo = [int(item) for item in codigo]

    return codigo
    
    


class syndrome_table:
    #Python class donde almacenamos la tabla de sindromes mas probables
    def __init__(self,q,k,n):

        self.q = q
        self.k = k
        self.n = n
        self.e_val = []
        self.syndr_val = []

    def __str__(self):

        return("Tabla de sindromes\nq: {}, k: {}, n: {}\nSyndr:{}\nErrors:{}\n".format(self.q,self.k,self.n,self.syndr_val,self.e_val))

    def search_syndrome(self,vector):
        
        for i in range(len(self.syndr_val)):

            if (bin_2_dec(self.syndr_val[i]) == bin_2_dec(vector)):

                return (self.e_val[i])

        return([-1])

    def add_sydrome(self,syndr,err_v):
        
        self.e_val.append(list(err_v))
        self.syndr_val.append(list(syndr))

    
def bin_2_dec(binary):
    return sum(val*pow(2,idx) for idx, val in enumerate(reversed(binary)))


def DecodificadorHamming(codigo,h):
    (q,n) = h.shape
    k = n - q

    max_msg = int(len(codigo)/n)
    err = 0
    err_no_corr = 0
    bits = []
    
    err_vect = np.eye(n, dtype = int)    #Todos los vectores de error con menos num de 1
    
    table = syndrome_table(q,k,n)

    #Para generar los sindromes correspondientes multiplicamos por H' (s = e*H')

    for i in range(err_vect.shape[0]):
        
        s = np.mod(np.dot(err_vect[i,:],np.transpose(h)),2)
        s = [int(item) for item in s]
        table.add_sydrome(s,err_vect[i,:])

    #Una vez generada la tabla de sindromes pasamos a reconstruir los bits enviados
   
    
    for i in range(max_msg):

        code_slice = codigo[i*n:(i+1)*n]
        syndrome = list(np.mod(np.dot(code_slice,np.transpose(h)),2))
        syndrome = [int(item) for item in syndrome]
     
        
    
        #Si el síndrome refleja un error lo buscamos y se corrige si es posible

        if (sum(syndrome) != 0):
            err += 1
            e = table.search_syndrome(syndrome)
          
            if(len(e)>1):          
                aux = np.mod(np.add(code_slice,e),2)
                bits.extend(aux[0:4])
                
            
        else:

            bits.extend(code_slice[0:4])


    print("Se han detectado un total de {} errores".format(err))
    
    return bits        
       








    