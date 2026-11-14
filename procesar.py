from modelos import Registro


mediciones = [24, 31, 28, 37, 26, 42, 29, 35, 23, 39]


def procesar(mediciones):
    lista_mediciones = []
    indice = 0

    for medicion in mediciones:
        print("posición",indice,"-->",medicion,"°C")
        indice = indice + 1

    return lista_mediciones



if __name__ == "__main__":

    procesar(mediciones)

