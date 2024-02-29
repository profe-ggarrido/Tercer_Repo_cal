import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Llamar a la función para limpiar la consola
limpiar_consola()


"""
DATOS IMPORTANTES PARA EL DESARROLLO DEL PROBLEMA
--------------------------------------------------
La velocidad de escape de un planeta es la velocidad mínima necesaria 
para que un objeto venciendo la gravedad del planeta pueda escapar de 
su campo gravitacional y viajar hacia el espacio exterior de forma indefinida. 
En otras palabras, es la velocidad que un objeto debe alcanzar para superar 
la atracción gravitatoria del planeta y no ser retenido por su campo gravitacional.

Matemáticamente, la velocidad de escape (Ve) se calcula utilizando la fórmula:

   Ve =  RAIZ² de(2 * G * R )
    Ve: es la velocidad de escape en metros por segundo (m/s).

    g: es la constante gravitacional del planeta en metros por segundo al cuadrado (m/s²).

    r es el radio del planeta en metros (m).

CASO 1
    DADOS LOS DATOS DE LA TIERRA
    ----------------------------

        g: 9.81 m/s
        r: 6.371 kms. (Radio de la Tierra; 6.371.000 mts.)

        Ve = Raiz² (2 * 9.81 m/seg.²) * 6.371.000  //// OJO el 2 no es elevado al cuadros
        ...
        Ve = 11,186 m/s



CASO 2
    DADOS LOS DATOS DE LA LUNA
    ----------------------------

        g: 1,62 m/s²
        r: 1,737 kms. (Radio de la Luna; 1.737.000 mts.)

        Ve = Raiz² (2 * 1,62 m/seg.) * 1.737.000 mts)
        ...
        Ve = 2,37 m/s 



"""

# zona de INPUT en la terminal
# 

planeta = input("Ingrese el nombre del planeta(Solo texto): " )
fuerza_g = float(input("Ingrese la fuerza 'g' del planeta (Solo numeros): ") )
radio_plane = float(input("Ingrese el 'radio'  del planeta (en mts.): ") )

# Calculo de la Ve
veloci_escape = round(( 2 * fuerza_g * radio_plane) ** 0.5 , 3)  # en mts/seg

#Aplicacion de formato numerico y decimales
veloci_escape_fmto = "{:,.4f}".format(veloci_escape)

# Conversión a KM/Hr
veloci_escape_kms = round(( 2 * fuerza_g * radio_plane) ** 0.5 , 3) * 3.6
veloci_escape_kms = "{:,.4f}".format(veloci_escape_kms)

#Limpiar la consola para mostrar resultados
limpiar_consola()

print("AHORA USTED VERÀ EL RESULTADO EN MTS/SEG Y ADEMAS EN KMS/HORA")
print("-------------------------------------------------------------")
print("")
print("La velocidad de escape para la(el) planeta " + planeta + " es : " + str(veloci_escape_fmto) + " mts/seg.")

#print(veloci_escape_kms)
print(" o : " + str(veloci_escape_kms) + " kms/hr.")
