#Diseñar un algoritmo que clasifique las notas de grado según el rango establecido

nota = float(input("Ingres la nota de grado: "))
if nota > 11:
    print("Nota Fuera de rango")
else:
    if nota >= 9:
        print("A")
    elif nota >= 8:
        print("B")
    elif nota >= 7:
        print("C")
    elif nota >= 6:
        print("D")
    elif nota < 6:
        print("E")


