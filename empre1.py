# COMPONENTES INICIALES
import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Llamar a la función para limpiar la consola
limpiar_consola()


# Peticion de datos

p = float(input("Ingese precio suscripcion: \n"))

u = float(input("Ingese numero de usuario: \n"))

gt = float(input("Ingese gasto total: \n"))

#CALCULO DE LA UTILIDAD

util = p * u - gt
print("El gasto total con los datos ingresados es: " + "{:,.2f}".format(util))


