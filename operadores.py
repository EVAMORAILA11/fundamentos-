def nuevoTema(tema):
    print(f"\n----- {tema} -----\n")

if __name__ == "__main__":
    
    nuevoTema("Operadores aritméticos")
    print("Suma 5 + 4 =", 5 + 4)
    print("Resta 5 - 3 =", 5 - 3)
    print("Multiplica 2 * 2 =", 2 * 2)
    print("División 2 / 2 =", 2 / 2)
    print("Exponente 2 ** 2 =", 2 ** 2)
    print("Residuo 15 % 4 =", 15 % 4)

    nuevoTema("Operadores lógicos")
    print("True and True =", True and True)
    print("True and False =", True and False)
    print("False and True =", False and True)
    print("False and False =", False and False)
    print("not False =", not False)
    print("True or True =", True or True)
    print("False or True =", False or True)

    nuevoTema("Operadores de comparación")
    print("5 == 5:", 5 == 5)
    print("6 != 5:", 6 != 5)
    print("10 > 4:", 10 > 4)

    nuevoTema("Variables")
    variable1 = 10
    _variable2 = 6.23
    Variable3 = "pepe"
    nomvariable = 8
    nombre_variable = 34.5
    print(variable1, _variable2, Variable3, nomvariable, nombre_variable)

    print("Declarar variables múltiples")
    a, b, c = 5, 10, 8  
    print(a)
    print(b)
    print(c)
    nombre_variable = "adios"
    print(nombre_variable)

    nuevoTema("Enteros")
    A = 105
    B = 1234566789012344

    C = -58
    D = 0b0011001
    E = 0xFF
    print("A:", A , type(A))
    print("B:", B , type(B))
    print("C:", C , type(C))
    print("D:", D , type(D))
    print("E:", E , type(E)) 

    nuevoTema("Flotantes")
    de = 1234.56
    print(de, type(de))
    den = -0.2587
    print(den, type(den))

    nuevoTema("Números complejos")
    x = -46j
    y = 12 + 45j
    z = 2j
    c = y + z
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(c, type(c))

    nuevoTema("Booleanos")
    x = True
    print(x, type(x))

    nuevoTema("listas")
    lista=[10,20.5,"lista"]
    print(lista) 
    print(lista[1])
    lista[0] = "hola"
    print(lista)
    print(lista[5])
    print(lista[5],[4])
    print(lista[3],[4])
    
    nuevoTema("Tuplas")
    tupla=(25,"Tupla", 1+10j)
    print(tupla)
    print(tupla[1])
    nuevoTema("conjunto")
    conjunto={10,20,30,40,50,20}
    print(conjunto)
    conjunto.add(80)
    print(conjunto) 
    nuevotema("diccionarios")
    direccionario={"nombre": "Consuelo","edad": 41, "teléfono": 23454567, 90:4+3j}
    print(diccionario)
    print(diccionario[nombre])
    print(diccionario[90] )
    nuevoTema("cadenas")
    cadena1 = "esto es una cadena"
    cadena2 = "Esto es otra cadena"
    cadena_multilinea = '''esto es una cadena cadena de varia lineas con tabuladores y saltos de linea'''
    print(cadena1, type(cadena1))
    print(cadena2, type(cadena2))
    print(cadena_multilinea, type(cadena_multilinea))
    cadena3="EVA" * 5
    print(cadena3)
    print(cadena1[2])
    print(cadena1[2:10])
    print(cadena1[:5])
    print(cadena1[:-5])
    print(cadena1[5:5])
    



              





