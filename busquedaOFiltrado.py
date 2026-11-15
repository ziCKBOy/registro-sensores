from modelos import Registro


mediciones = [24, 31, 28, 37, 26, 42, 29, 35, 23, 39]

def busquedaSecuencial(mediciones, condicion):
    lista_mediciones = []
    encontrada = False

    for medicion in mediciones:
        if medicion == condicion:
            print(f"la medicion {medicion} es igual a {condicion}")
            encontrada=True
            break

def filtroSecuencial(mediciones, condicion):
    lista_mediciones = []
    encontrada = False
    indice = 0
    conteo = 0
    for medicion in mediciones:
        if medicion > condicion:
            lista_mediciones.append(medicion)
            conteo=conteo+1

        indice=indice+1

    print(f"Se encontró un total de {conteo} mediciones sobre 30")
    return lista_mediciones


def elegirEstrategia(mediciones):

    lista_mediciones = filtroSecuencial(mediciones, 30)
    medicion = busquedaSecuencial(mediciones, 35)



if __name__ == "__main__":

    elegirEstrategia(mediciones)
