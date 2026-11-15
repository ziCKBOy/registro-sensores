from modelos import Registro


mediciones = [24, 31, 28, 37, 26, 42, 29, 35, 23, 39]


def filtroSecuencial(mediciones):
    lista_mediciones = []
    encontrada = False
    indice = 0
    conteo = 0
    for medicion in mediciones:
        if medicion > 30:
            print(f"la medicion {medicion} con indice {indice} es mayor a 30")
            conteo=conteo+1

        indice=indice+1

    print(f"Se encontró un total de {conteo} mediciones sobre 30")



if __name__ == "__main__":

    filtroSecuencial(mediciones)
