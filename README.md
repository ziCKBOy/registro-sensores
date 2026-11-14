# Registro de sensores

Actividad sumativa de la Universidad Central: operaciones básicas sobre una colección de 10 mediciones de un sensor (indexación, recorrido y búsqueda secuencial), implementadas en Python.

## Datos de ejemplo

Todos los scripts trabajan con la misma lista de mediciones:

```python
mediciones = [24, 31, 28, 37, 26, 42, 29, 35, 23, 39]
```

## Estructura del proyecto

| Archivo | Descripción |
| --- | --- |
| `modelos.py` | Define la clase `Registro` (`id`, `medicion`) como `dataclass`. |
| `indexar.py` | Parte 1. Almacena las mediciones en una lista, muestra la medición 4, reemplaza el valor de la posición 2 por 30 y lo vuelve a mostrar. |
| `procesar.py` | Parte 2. Recorre la colección e imprime cada posición con su medición en °C. |
| `busquedaSecuencial.py` | Parte 3. Búsqueda secuencial del valor 42 en la colección. |
| `Becerra_Oliver_Actividad_sumativa_S3_U3.docx` | Informe de entrega con el código de cada parte. |
| `003_Actividad_Sumativa.pdf` | Enunciado de la actividad. |
| `07.b.S3_9915003_Rubrica_1_actividad_individual.pdf` | Rúbrica de evaluación. |

## Requisitos

- Python 3.7 o superior (se usa `dataclasses`). Probado con Python 3.14.
- No requiere librerías externas.

## Uso

Ejecuta cada script desde la carpeta del proyecto:

```bash
python indexar.py
python procesar.py
python busquedaSecuencial.py
```

### Salida de ejemplo

`procesar.py`:

```
posición 0 --> 24 °C
posición 1 --> 31 °C
...
posición 9 --> 39 °C
```

`busquedaSecuencial.py`:

```
la medicion es igual a 42
¿encuentra valor? True
```

## Autor

Oliver Becerra
