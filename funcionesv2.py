print("Funciones version 2")
print("Reyes Ramirez")
# Zona de listas tuplas set y diccionario
celulares=["Samsung a52","Iphone 11","Chafa"]

nombreperros = ("flash", "chato", "gooffy")

estadosdemexico = {"Chihuahua", "Durango", "Sinaloa"}

computadoras = {
  "Apple": "Macbook12",
  "Samsung": "Samsung laptop i32",
  "huawei": "pc gaming3"
}

# Zona de funciones
def verlista(Telefonos):
    for uncelular in Telefonos:
        print(uncelular)

def perrolista(Perros):
    for unperro in Perros:
        print(unperro)

def estadoslista(Estados):
    for unestado in Estados:
        print(unestado)

def compulista(computadoras):
    for x, y in computadoras.items():
        print(x, y)

# Llamadas de funciones
print("Imprime celulares")
verlista(celulares)

print("Imprime Nombres de perros")
perrolista(nombreperros)

print("Imprime Nombres de estados de mexico")
estadoslista(estadosdemexico)

print("Imprime Nombre de computadora")
compulista(computadoras)
