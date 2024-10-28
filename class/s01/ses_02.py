lista = [1, True, 3.6, "Cadena de caracteres", 6, 7, 8, 9]
days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sundayyyyyy', lista]
#      0            1        2            3           4         5           6
                                                  #  -3        -2           -1
print(days)

print(days[0])
print(days[1])
print(days[2])

days[6] = 'Sunday'
print(days)

print(days[-1])

print("Longitud de la lista: ", len(days))

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]    
]

print(matriz)
print(matriz[0])
print(matriz[0][0])
print(matriz[2][2])
matriz[2][2] = 100
print(matriz)


# Diccionario
diplomado = {
    "nombre": "Diplomado en aprendizaje automatico",
    "programa": "Ingeniería de sistemas",
    "dias_de_clase": days
}

print(diplomado)
print(diplomado["nombre"])
print(diplomado["programa"])

