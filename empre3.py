#  *** E M P R E 3 *****
# -----------------------


# COMPONENTES INICIALES
import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Llamar a la función para limpiar la consola
limpiar_consola()


# Peticion de datos


# Peticion de datos EMPRE2

print("ESCENARIO Nro. 3")
print("-------------------")
print("")


p = float(input("Ingese precio suscripcion: \n"))

u = float(input("Ingese numero de usuario: \n"))

gt = float(input("Ingese gasto total: \n"))

ua = float(input("Ingese la utilidad del año anterior: \n"))


#CALCULO DE LA UTILIDAD

util = p * u - gt

rz = util / ua

# presentacion por COnsola
print("La utilidad actual es: " + "{:,.2f}".format(util))

print("La razon/proporcion con el año anterior es: " + "{:,.2f}".format(rz))

