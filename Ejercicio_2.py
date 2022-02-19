#Diseñar un algoritmo que presente el resultado de las operaciones matemáticas.

lista1 = list(range(1,4))
lista2 = list(range(1,4))
lista3 = list(range(1,4))

indice = 0
for i in lista1:
    result = i * 1
    indice += 1
    print( 1, "* ", indice , "=", result )
indice2 = 0
for i in lista1:
    result = i * 2
    indice2 += 1
    print( 2, "* ", indice2 , "=", result )
indice3 = 0
for i in lista1:
    result = i * 3
    indice3 += 1
    print( 3, "* ", indice3 , "=", result )

