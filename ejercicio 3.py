print("Programa piedra, papel o tijera")
import random
rondas = 3
rondaActual = 0
puntajeJugador = 0
puntajePc = 0
lista = ["Piedra", "Papel", "Tijera"]
while rondaActual < rondas:
    rondaActual += 1
    print("ronda", rondaActual)
    persona  = input("Piedra/papel/tijeras?")
    pc = (random.choice(lista))
    print("La pc sleccionó", pc)
if persona == "piedra" and pc == "tijera":
    puntajeJugador += 50
    print(("Ganaste") + str(puntajeJugador)+ "pts")
elif persona == "papel" and pc == "piedra":
    print("trabajando")



