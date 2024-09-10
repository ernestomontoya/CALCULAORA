def sumar():
    pass

# 5 - 4 - 3 - 2 - 1

def mi_funcion_recursiva(repetir):
    retorno = 1

    print (repetir)
    if repetir > 1:
        retorno = mi_funcion_recursiva(repetir -1)

    return retorno

def calcular_factorial(numero:int)-> int:
    retorno = 1

#mi_funcion_recursiva(5)