# Practica2_Comunicaciones_Digitales
# Miguel Antunes Garcia 

Los ejercicios se ejecutan en Ejercicios.py, en el cual se llaman a las funciones necesarias guardadas en el resto de archivos.

    python Ejercicios.py -n [Número de ejercicio]

    1.Códigos de repetición: 

        Se muestran los primeros bits a enviar, el mensaje con repetición, el mensaje recibido tras pasar por el canal y la decodificación.
        Se calcula la probabilidad de error para el mensaje enviado de 10000 bits y debe dar un valor similar al teórico.

    2.Códigos de paridad:

        Al igual que en el caso de repetición se envían 10000 bits mostrando una muestra del mensaje original, su codificación, su salida del canal y su decodificación. Para este caso si se detecta un error no es posible corregirlo, luego se marcan todos los bits del mensaje como erróneos (en el caso de que haya 3 errores esto es correcto, pero si solo hay uno el algoritmo marca a los tres).
        Por último también se ha calculado la probabilidad de que no se detecte el error (número par de errores en el mensaje).

    3.Códigos bloque:

        En primer lugar se calculan las matrices G y H. Al igual que los casos anteriores, se plantea enviar 10000 bits de información de los que se representan los primeros bits y sus correspondientes mensajes enviados y recibidos por el canal y el receptor final. En este caso se calcula los errores que aparecen tanto a la salida del canal como una vez decodificado el mensaje, para comprobar la mejora que introduce utilizar Hamming para detección y corrección.

        Una vez comprobado el funcionamiento con bits, se va a comprobar el efecto en una cadena de texto de "Don Quijote" siguiendo el siguiente proceso:
            -Cada caracter de la cadena se transforma en su identificador numérico ASCII. ´a´ --> 97
            -El identificador se transforma a binario. 97 --> 01100001
            -Se repite el proceso para todos los caracteres concatenando los valores binarios.
            -Se aplica Hamming a los valores binarios.
            -En el receptor, se decodifica Hamming y se corrigen los errores que sean posibles.
            -Se deshace la transformación binaria para recuperar el valor ASCII y por consiguiente el caracter.

        Para comprobar la eficacia de la corrección de errores de Hamming, se representa la cadena sin y con corrección, comprobando que la mayoría de errores se corrigen. Cada vez que se ejecuta los errores en los bits cambian, y por lo tanto el resultado también, un ejemplo de ejecucción sobre la cadena de texto:

            
            En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor

            Se han detectado un total de 42 errores

            Texto con errores corregidos:
            En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho que.vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor
            
            Texto sin corrección:
            Un un $ugar de la Mancha<(de cuyo noíbre$No quiero acordarme, fo ha mushï que,vivía`un hmdalgo `e hos du lanza en a3tiLlero, c`arga antiwua, socí. flaãO y galgo corredos

Las funciones de cada apartado están en un archivo diferente

Librerías utilizadas:

    -Argparse 1.1
    -OS 
    -Platform 1.0.8
    -Math 
    -NumPy 1.20.2
    -Random 
