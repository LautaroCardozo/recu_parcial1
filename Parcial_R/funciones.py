from random import randint

#1
def pedir_numero_lista(mensaje:str)->int:
    """La funcion permite pedir un numero de lista al usuario y lo valida (que no sea alfabetico,que sea mayor a cero y que contenga 3 caracteres)

    Args:
        mensaje (str): Mensaje que se muestra por consola

    Returns:
        int: Numero de lista ingresado,validado
    """
    numero_lista = input(f"{mensaje}")
    while numero_lista.isalpha():
        numero_lista = input(f"El numero de lista no puede contener letras.Reingrese numero de lista: ")
    while int(numero_lista) < 0:
        numero_lista = input(f"El numero de lista no puede ser menor a cero.Reingrese numero de lista: ")
    while int(numero_lista) > 999:
        numero_lista = input(f"El numero de lista debe tener 3 caracteres.Reingrese numero de lista: ")
    return int(numero_lista)

def pedir_votos(mensaje:str)->int:
    """La funcion permite pedir una cantidad de votos al usuario y lo valida (que no sea alfabetico y que sea mayor a cero)

    Args:
        mensaje (str): Mensaje que se muestra por la consola

    Returns:
        int: Cantidad de votos ingresada,validada
    """
    votos = input(f"{mensaje}")
    while votos.isalpha():
        votos = input(f"La cantidad de votos no puede contener letras.Reingrese numero de lista: ")
    while int(votos) < 0:
         votos = input(f"La cantidad de votos no puede ser menor a cero.Reingrese numero de lista: ")
    return int(votos)
    


def cargar_votos(matriz:list)->None:
    """Recibe una matriz y permite realizar la carga de los datos,numero de lista y cantidad de votos

    Args:
        matriz (list): Matriz a cargar
    """
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil]) -1):
            if col == 0:
                numero_lista = pedir_numero_lista("Ingrese el numero de lista: ")
                matriz[fil][col] = numero_lista
            else:
                if col == 1:
                    votos = pedir_votos("Ingrese la cantidad de votos que recibio del turno mañana: ")
                elif col == 2:
                    votos = pedir_votos("Ingrese la cantidad de votos que recibio del turno tarde: ")
                else:
                    votos = pedir_votos("Ingrese la cantidad de votos que recibio del turno noche: ")
                matriz[fil][col] = votos 
#2
def mostrar_matriz(matriz:list)->None:
    """Recibe una matriz (hasta 5 columnas) y muestra sus contenidos por consola

    Args:
        matriz (list): Matriz a mostrar
    """
    if type(matriz) == list:
        for fil in range(len(matriz)):
            print(f"El partido lista {matriz[fil][0]} recibio:\n Votos del turno mañana = {matriz[fil][1]}\n Votos del turno tarde = {matriz[fil][2]}\n Votos del turno noche = {matriz[fil][3]}\nPorcentaje de votos lista {matriz[fil][0]} = {matriz[fil][4]:.2f}")
    else:
        print("Debe ingresar una matriz")

#3
def ordenar_matriz(matriz:list,indice:int)->list:
    """Recibe una matriz y un indice para comparar y ordenar de mayor a menor 

    Args:
        matriz (list): Matriz
        indice (int): Indice criterio

    Returns:
        list: Matriz ordenada
    """
    if type(matriz) == list and type(indice) == int:
        for fil_i in range(len(matriz) - 1):
            for fil_j in range(fil_i + 1, len(matriz)):
                if matriz[fil_i][indice] < matriz[fil_j][indice]:
                    aux = matriz[fil_i]
                    matriz[fil_i] = matriz[fil_j]
                    matriz[fil_j] = aux
    else:
        print("Debe ingresar los formatos correctos")
        

#4
def calcular_total_votos(matriz:list)->int:
    """Recibe una matriz,suma todos los valores dentro de los indices 1,2 y 3 y devuelve dicha suma

    Args:
        matriz (list): Matriz de votacion

    Returns:
        int: Cantidad total de votos
    """
    if type(matriz) == list:
        total_votos = 0
        for fil in range(len(matriz)):
            for col in range(1,len(matriz[fil])):
                if type(matriz[fil][col]) == int:
                    total_votos = total_votos + int(matriz[fil][col])
                else:
                    print("La matriz solo puede contener numeros")
                    break
    else:
        print("Debe ingresar una matriz")
    return total_votos

def calcular_porcentaje_votos(matriz:list)->None:
    """Recibe una matriz,cuenta los votos,calcula el porcentaje y agrega a la matriz de porcentajes el mismo

    Args:
        matriz (list): Matriz de votacion
    """
    votos_totales = calcular_total_votos(matriz)
    for fil in range(len(matriz)):
        votos_recibidos = 0
        for col in range(1,len(matriz[fil]) -1):
            votos_recibidos += int(matriz[fil][col])
            if votos_totales > 0:
                porcentaje = (votos_recibidos/votos_totales) * 100
                matriz[fil][4] = porcentaje
            else:
                print("No se puede dividir por cero")

#4
def encontar_menos_votados(matriz:list,limite:int)->list:
    """Recibe una matriz y un limite,arma una nueva matriz con todas las filas cuyo porcentaje de votos sea menor al limite

    Args:
        matriz (list): Matriz de votacion
        limite (int): Numero al que el porcentaje de votos debe ser menor

    Returns:
        list: Matriz de menos votados
    """
    matriz_menos_votados = []
    for fil in range(len(matriz)):
        if matriz[fil][4] < limite:
            matriz_menos_votados += [matriz[fil]]

    return matriz_menos_votados

#5
def hallar_turno_mas_votos(matriz:list)->None:
    """Calcula el turno/turnos que mas voto

    Args:
        matriz (list): Matriz de votacion
    """
    if type(matriz) == list:
        votos_mañana = 0
        votos_tarde = 0
        votos_noche = 0
        votos_maximos = None
        for fil in range(len(matriz)):
            for col in range(1,len(matriz[fil])-1):
                if col == 1:
                    votos_mañana += matriz[fil][col]
                elif col == 2:
                    votos_tarde += matriz[fil][col]
                else:
                    votos_noche += matriz[fil][col]
        if votos_mañana > votos_tarde and votos_mañana > votos_noche:
            votos_maximos = votos_mañana
        elif votos_tarde > votos_mañana and votos_tarde > votos_noche:
            votos_maximos = votos_tarde
        elif votos_noche > votos_tarde and votos_noche > votos_tarde:
            votos_maximos = votos_noche
        print("El/los turno(s) que mas voto es/son: ")
        if votos_maximos == votos_mañana:
            print(f"-Turno mañana con {votos_mañana} votos")
        if votos_maximos == votos_tarde:
            print(f"-Turno tarde con {votos_tarde} votos")
        if votos_maximos == votos_noche:
            print(f"-Turno noche con {votos_noche} votos")   
    else:
        print("Debe ingresar una matriz")
        
#6
def verificar_ballotage(matriz:list)->bool:
    """Verifica si se hace una ballotage

    Args:
        matriz (list): Matriz de votacion

    Returns:
        bool: True si hay ballotage (Ninguno de los candidatos supero el 50% de los votos),false caso contrario
    """
    if type(matriz) == list:
        ballotage = True
        for fil in range(len(matriz)):
            if matriz[fil][4] > 50:
                ballotage = False
                break
            else:
                ballotage = True
        return ballotage

#7
def calcular_votos_random(votos:int)->int:
    """Recibe una cantidad de votos y devuelve un numero entre 0 y el que se introdujo originalmente

    Args:
        votos (int): Cantidad de votos

    Returns:
        int: Cantidad de votos random
    """
    if type(votos) == int:
        voto_random = randint(0,votos)
        return voto_random
    else:
        print("Debe ingresar una numero")

def realizar_ballotage(matriz:list)->None:
    """Lleva a cabo el ballotage

    Args:
        matriz (list): Matriz de votacion
    """
    ordenar_matriz(matriz,4)
    matriz_ballotage = [[matriz[0][0],0,0,0,0],
                        [matriz[1][0],0,0,0,0]]
    total_votos_mañana = pedir_votos("Ingrese el total de votos que se registraron a la mañana: ")
    total_votos_tarde = pedir_votos("Ingrese el total de votos que se registraron a la tarde: ")
    total_votos_noche = pedir_votos("Ingrese el total de votos que se registraron a la noche: ")
    votos_mañana = calcular_votos_random(total_votos_mañana)
    votos_tarde = calcular_votos_random(total_votos_tarde)
    votos_noche = calcular_votos_random(total_votos_noche)
    resto_votos_mañana = total_votos_mañana - votos_mañana
    resto_votos_tarde = total_votos_tarde - votos_tarde
    resto_votos_noche = total_votos_noche - votos_noche
    matriz_ballotage[0][1] = votos_mañana
    matriz_ballotage[0][2] = votos_tarde
    matriz_ballotage[0][3] = votos_noche
    matriz_ballotage[1][1] = resto_votos_mañana
    matriz_ballotage[1][2] = resto_votos_tarde
    matriz_ballotage[1][3] = resto_votos_noche
    ordenar_matriz(matriz_ballotage,4)
    calcular_porcentaje_votos(matriz_ballotage)
    mostrar_matriz(matriz_ballotage)


def ejecutar_menu(matriz:list)->None:
    """Ejecuta un menu con 8 opciones
    """
    ejecutar = True
    ballotage = None
    verifico_ballotage = False
    while(ejecutar):
        print("Opciones")
        opcion = int(input("1-Cargar datos\n2-Mostrar datos\n3-Ordenar datos\n4-Mostrar candidatos con votos menores al 5%\n5-Mostrar el/los turnos que mas votaron\n6-Verificar si hay ballotage\n7-Realizar ballotage\n8-Salir\nIngrese opcion: "))
        if opcion == 1:
            cargar_votos(matriz)
        elif opcion == 2:
            calcular_porcentaje_votos(matriz)
            mostrar_matriz(matriz)
            input("Presione enter para continuar...")
        elif opcion == 3:
            ordenar_matriz(matriz,1)
            mostrar_matriz(matriz)
            input("Presione enter para continuar...")
        elif opcion == 4:
            menos_votados = encontar_menos_votados(matriz,5)
            mostrar_matriz(menos_votados)
            input("Presione enter para continuar...")
        elif opcion == 5:
            hallar_turno_mas_votos(matriz)
            input("Presione enter para continuar...")
        elif opcion ==  6:
            ballotage = verificar_ballotage(matriz)
            verifico_ballotage = True
            if ballotage:
                print("Hay ballotage")
                input("Presione enter para continuar...")
            else:
                print("No hay ballotage")
                input("Presione enter para continuar...")
        elif opcion == 7 :
            if verifico_ballotage:
                realizar_ballotage(matriz)
                input("Presione enter para continuar...")
            else:
                print("Debe verificar si hay ballotage")
        elif opcion ==  8:
            ejecutar = False 
           