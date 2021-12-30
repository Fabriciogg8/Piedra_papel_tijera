import random


def piedra_papel_tijera(func):
    def wrapper(*args, **kwargs):
        lista_jugadas = ["piedra", "papel", "tijera"]
        jugada = random.choice(lista_jugadas)
        print(f"La PC muestra {jugada}")
        func(*args, **kwargs)
        if jugada == "piedra" and mano == "papel" \
           or jugada == "papel" and mano == "tijera"\
           or jugada == "tijera" and mano == "piedra":
            print("Ganaste")
        elif jugada == mano:
            print("empate")
        else:
            print("perdiste")
    return wrapper


mano = "papel"
@piedra_papel_tijera
def mi_turno(mano: int):
    print(f"Yo muestro {mano}")


if __name__ == "__main__":
   mi_turno(mano) 

