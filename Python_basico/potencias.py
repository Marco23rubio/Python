def elevacion(numero):
    potenciador = 0
    resultado = numero**potenciador
    while resultado <1000:
        print(f"El valor de {numero} elevado a la potencia {potenciador} es igual a = {resultado}")
        potenciador += 1
        resultado = numero**potenciador
        
        

def run():
    numero = int(input("Escoge un numero para elevar= "))
    elevacion(numero)


if __name__ == "__main__":
    run()
