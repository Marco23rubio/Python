def sumasion(min,max):
    print("Bienvenido a la calculadora capaz de sumar numeros consecutivos, a continuación solo necesitaras escoger tu rango de numeros para realizar la suma. 👀")
    min = int(input("Pon aqui el valor minimo= "))
    max = int(input("Pon aqui el valor maximo= "))
    sumador = min + 1
    x = 1
    while x < max:
        suma = min + sumador
        min = min + sumador
        sumador +=1
        x +=1
    print(suma)



sumasion(min,max)



  
   
