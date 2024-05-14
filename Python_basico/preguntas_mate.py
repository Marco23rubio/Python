

def run():
    
    menu= input("""¿Estas listo para tu examen?
        1)Si, estoy listo
        2)No, aun no lo estoy
        respuesta: """)
    decision = int(menu)
    while decision != 1:
        print("""
        Tranquilo tomate tu tiempo para estudiar""")
        menu= input("""
        ¿Estas listo para tu examen?
        1)Si, estoy listo
        2)No, aun no lo estoy
        respuesta: """)
        decision = int(menu)
        
    p1=input("""
    La primera pregunta es:
    ¿Cuanto es 9x9?
    """)
    r1=int(p1)
    while r1 !=81:
        print("""Lo siento esa no es la respuesta intentalo de nuevo
        """)
        p1=input("""
    La primera pregunta es:
    ¿Cuanto es 9x9?
        """)
        r1=int(p1)
    print("""
    Sacaste 100 c:
    """)
        
        
        
            



 

    
if __name__ == "__main__":
    run()
