import numpy as np
import math

def MatricesHamming(q):

    values = np.arange(pow(2,q))
    values = np.delete(values,0)

    for value in values:

        print(value)
        binary = format(value,"b").zfill(q)
        for element in binary:
            print(element)