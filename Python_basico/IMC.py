peso = float(input("Cual es tu peso?(en Kg)"))
altura = float(input("Cual es tu altura?(en metros)"))

bmi = round(peso/altura**2,2)

def imc(y):
    print("Su IMC es de: " +str(bmi)+ " . Se encuentra en la categoría de: " +y)

if bmi < 18.5 and bmi >0 :
    imc("Bajo de peso")
elif bmi >= 18.5 and bmi <25:
    imc("Peso normal")
elif bmi >=25 and bmi <30:
    imc("Sobrepeso")
elif bmi >=30:
    imc("Obesidad")
else:
    print("A ocurrido un error, intentelo de nuevo")
