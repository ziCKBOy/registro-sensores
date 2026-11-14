from modelos import Registro


mediciones = [24, 31, 28, 37, 26, 42, 29, 35, 23, 39]


def busquedaSecuencial(mediciones):
    lista_mediciones = []
    encontrada = False

    for medicion in mediciones:
        if medicion == 42:
            print("la medicion es igual a 42")
            encontrada=True
            break

    print("¿encuentra valor?",encontrada)


if __name__ == "__main__":

    busquedaSecuencial(mediciones)
