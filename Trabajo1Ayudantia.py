
#La ejecucion se realizo en ipython netbook

#Trabajo 1 Ayudantia

#Paula Lineros E.
#Franco Morales B.
#Victoria Muñoz B.
#Pedro Salas V.



n = 600851475143

def mayor_factor_primordial(n):
 
    mayor_factor = 1
 
    # Elimina los factores de 2
    while n % 2 == 0:
        mayor_factor = 2
        n = n/2
 
    # busca los factores impares
    f = 3
    while n != 1:
        while n % f == 0:
            mayor_factor = f
            n = n/f
        f += 2
 
    return mayor_factor
 
for i in range(100000): a = mayor_factor_primordial(n)
    
   # imprime el resultado  
print "El mayor factor primordial de %s es : %s  "% (n,a)
