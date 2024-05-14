print(
"""
Hola, bienvenido al motor de busqueda de palabras, que te ayuda a encontrar si una palabra se encuentra en un texto
Por lo que debes hacer es ingresar el texto donde se buscara la palabra y después ingresar que palabra es la que 
deseas encontrar , ¿Listo?
""")

texto = str(input("Pon aqui el texto donde se realizará la busqueda: "))
palabra = str(input("Pon aqui la palabra que deseas buscar: "))

def search():
    if palabra in texto:
        print("Word found")
    else:
        print("Word not found")

search()
