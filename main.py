"""Inicio
mostrar "ingrese respuestas correctas, incorrectas y en blanco"
mostrar "Ingrese respuestas correctas"
ingrese respuestas correctas
mostrar "respuestas incorrectas"
ingrese respuestas incorrectas
mostrar "respuestas en blanco"
ingrese respuestas en blanco
mostrar "las respuestas correctas valen 4 puntos" respuestas correctas
mostrar "las respuestas incorrectas valen -1 punto" respuestas incorrectas
mostrar "las respuestas en blanco valen 0" respuestas en blanco
fin
"""

print("Programa puntaje")
correctas = input("Ingrese respuestas correctas:")
incorrectas = input("Ingrese respuestas incorrectas:")
blanco = input("Ingrese respuestas en blanco:")
puntajeCorrecto = int(correctas) * 4
puntajeIncorrectas = int(incorrectas) * -1
puntajeBlanco = int(blanco) * 0
print("Puntaje correcto es:", puntajeCorrecto)
print("Puntaje incorrecto es:", puntajeIncorrectas)
print("Puntaje en blanco es:", puntajeBlanco)
puntajeFinal = puntajeCorrecto + puntajeIncorrectas + puntajeBlanco
print("Puntaje final:",puntajeFinal)

if puntajeFinal < 30:
    print("Bien! Eres un duro")
else:
    print("No sirves inutil")