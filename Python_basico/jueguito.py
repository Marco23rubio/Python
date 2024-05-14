import random 


def run():
    print("""
    Bienvenido al juego de Encuentra el número :333333
    Las reglas son simples solo necesitas encontras el numero
    pensado por la máquina entre el 1 y el 100, si fallas
    la máquina te dira si debes buscar un numero mayor o menor
    pero cuidado, solo tienes 5 vidas, ¿Estas listo?

    """)
    numero_aleatorio = random.randint(1,100)
    vidas = 5
    numero_escogido = int(input("Escoge un numero del 1 al 100: "))
    vidas -=1 
    while numero_aleatorio != numero_escogido:
        print(f"Cantidad de vidas: {vidas}")
        vidas -=1
        if numero_escogido < numero_aleatorio:
            numero_escogido = int(input("Busca un numero mayor: "))            
        elif numero_escogido > numero_aleatorio:
            numero_escogido = int(input("Busca un numero menor: "))           
        elif numero_aleatorio == numero_escogido:
            print("Felicidades, has ganado")
        if vidas ==0:
            print("Game Over")
            break 
        
        
        

            
if __name__ == "__main__":
    run()