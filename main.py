# Lista de nombres
nombres = [ "Harry Houdini", "Newton", "David Blaine", "Hawking",
                "Messi", "Teller", "Einstein", "Pele", "Juanes"]

# Agregar El gran
def hacer_grandioso(magos):
#Agregamos un contador
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]

#  Imprimir nombres
def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)

# Separar en 3 grupos
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = [nombre for nombre in nombres
         if nombre not in magos and nombre not in cientificos]

# Imprimir la lista completa antes de ser modificada
print("\nLista original:")
imprimir_nombres(nombres)

# Imprimir los nombres de los magos
print("\nNombre de magos (sin el gran):")
imprimir_nombres(magos)

# Modificar magos
hacer_grandioso(magos)

# Imprimir magos grandiosos
print("\nLista de magos grandiosos:")
imprimir_nombres(magos)

# Imprimir científicos
print("\nLista de científicos:")
imprimir_nombres(cientificos)

# Imprimir los otros nombres
print("\nLista de otros nombres:")
imprimir_nombres(otros)

#imprimir lista modificada
total=["Newton","Hawking","Einstein","Messi","Pele","Juanes","EL gran Harry Houdini",
       "El gran David Blaine","El gran Teller"]
print("\nLISTA FINAL:")
imprimir_nombres(total)
