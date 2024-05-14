menu = """
Bienvenido al conversor de pesos a USD 😎

1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opción
"""
opcion = input(menu)

def precios(moneda,vd):
    pesos = float(input("Coloca la cantidad de Pesos "+moneda+":"))
    valor_dolar = vd
    dolares = str(round(pesos/valor_dolar,2))
    print("Tienes la cantidad de: "+dolares+ " USD")
    
if opcion == "1":
    precios("colombianos",300)
elif opcion== "2":
    precios("argentinos",50)
elif opcion== "3":
    precios("mexicanos",21)
else :
    print("Ingresa una opción valida")


