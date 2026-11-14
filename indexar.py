from modelos import Registro


mediciones = [24, 31, 28, 37, 26, 42, 29, 35, 23, 39]


def indexar(mediciones):
    lista_mediciones = []
    indice = 0

    for medicion in mediciones:
        lista_mediciones.append(medicion)
        indice = indice + 1

    return lista_mediciones


if __name__ == "__main__":

    medicionesIndexadas = indexar(mediciones)
    print(medicionesIndexadas);
    print("medicion 4: ", medicionesIndexadas[3])
    print("cambio valor de medición 2 a 30");
    medicionesIndexadas[1]=30
    print(medicionesIndexadas)
    print("medicion 2: ", medicionesIndexadas[1])
