print("Bienvenido al parque de diversiones más grande de Guayaquil")
estatura = int(input("¿Cuál es su estatura en centímetros?:"))
edad = int(input("¿Cuál es su edad?:"))
if estatura > 120 :
    print("Adelante mi amigo")
    if edad < 12 :
       print("son 5$")
    elif edad > 12 and edad < 18 :
       print("son $7")
    else:
       print("son 12$")
else:
 print("Larguese")







