#  *** E M P R E 2 *****
# -----------------------

#  COMPONENTES INICIALES
import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Llamar a la función para limpiar la consola
limpiar_consola()


# Peticion de datos EMPRE2

print("ESCENARIO NrO 2")
print("-------------------")
print("")

p = float(input("Ingese precio suscripcion: \n"))

un = float(input("Ingese numero de usuario NORMAL: \n"))

up = float(input("Ingese numero de usuario PREMIUM: \n"))

gt = float(input("Ingese gasto total: \n"))

#CALCULO DE LA UTILIDAD

util_n = p * un - gt

util_p = p * up * 1.5 - gt

# presentacion resultador de ambos tipos d Usuarios
print("La utilidad con los datos ingresados para usuarios Normales es: " + "{:,.2f}".format(util_n))

print("La utilidad con los datos ingresados para usuarios Premium es: " + "{:,.2f}".format(util_p))


