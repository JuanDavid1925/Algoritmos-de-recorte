
# Definimos códigos para identificar cada región
ADENTRO = 0  # 0000
IZQUIERDA = 1  # 0001
DERECHA = 2  # 0010
ABAJO = 4  # 0100
ARRIBA = 8	 # 1000


# Función que nos dice en que región se encuentra un punto determinado (x,y).
def posicionPunto(x, y, x_min, y_min, x_max, y_max):
    # iniciamos asumiendo que se encuentra adentro
    codigo = ADENTRO
    if x < x_min:	 # El punto se encuentra a la izquierda
        codigo |= IZQUIERDA
    elif x > x_max:  # El punto se encuentra a la derecha
        codigo |= DERECHA
    if y < y_min:	 # El punto se encuentra abajo
        codigo |= ABAJO
    elif y > y_max:  # El punto se encuentra arriba
        codigo |= ARRIBA

    return codigo


# Recortamos una linea desde P1 = (x1,y1) hasta P2 = (x2,y2)
# x_max, y_max, x_min, y_min nos permiten definir las dimensiones de la pantalla.
def cohenSutherlandRecorte(x_min, y_min, x_max, y_max, x1, y1, x2, y2):

    # verificamos en que posición están ambos puntos con respecto a las 9 regiones
    codigo1 = posicionPunto(x1, y1, x_min, y_min, x_max, y_max)
    codigo2 = posicionPunto(x2, y2, x_min, y_min, x_max, y_max)
    # Iniciamos asumiendo que la linea no está adentro de la ventana
    estaAdentro = False

    while True:

        # Ambos puntos están dentro de la ventana
        if codigo1 == 0 and codigo2 == 0:
            estaAdentro = True
            break

        # Ambos puntos están fuera de la ventana
        elif (codigo1 & codigo2) != 0:
            break

        # Algún segmento se encuentra dentro de la ventana
        else:

            # la línea necesita recorte
            # Al menos uno de los puntos está fuera
            x = 1.0
            y = 1.0
            if codigo1 != 0:
                codigo_afuera = codigo1
            else:
                codigo_afuera = codigo2

            # Encontrando el punto de intersección
            if codigo_afuera & ARRIBA:
                # El punto está encima del rectángulo de recorte
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max

            elif codigo_afuera & ABAJO:

                # El punto está debajo del rectángulo de recorte
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min

            elif codigo_afuera & DERECHA:

                # El punto está a la derecha del rectángulo de recorte
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif codigo_afuera & IZQUIERDA:

                # El punto está a la izquierda del rectángulo de recorte
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            # Reemplazamos el punto fuera del rectángulo de recorte.
            # por el punto de intersección
            if codigo_afuera == codigo1:
                x1 = x
                y1 = y
                codigo1 = posicionPunto(x1, y1, x_min, y_min, x_max, y_max)

            else:
                x2 = x
                y2 = y
                codigo2 = posicionPunto(x2, y2, x_min, y_min, x_max, y_max)

    if estaAdentro:
        print("Línea aceptada desde (%.2f , %.2f ) hasta (%.2f , %.2f)" %
              (x1, y1, x2, y2))

    else:
        print("Línea rechazada")


print("Defina el tamaño de la pantalla ")
x_min = input(
    "Ingrese la coordenada x de la esquina inferior izquierda (EII): ")
y_min = input(
    "Ingrese la coordenada Y de la esquina inferior izquierda (EII): ")
x_max = input(
    "Ingrese la coordenada x de la esquina superior derecha (ESD): ")
y_max = input(
    "Ingrese la coordenada y de la esquina superior derecha (ESD): ")
print("Defina las coordenadas de los puntos a dibujar ")
x1 = input("Ingrese la coordenada x del primer punto: ")
y1 = input("Ingrese la coordenada y del primer punto: ")
x2 = input("Ingrese la coordenada x del segundo punto: ")
y2 = input("Ingrese la coordenada y del segundo punto: ")


cohenSutherlandRecorte(int(x_min), int(y_min), int(x_max), int(y_max), int(x1),
                       int(y1), int(x2), int(y2))
