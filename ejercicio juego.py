# Piedra, Papel o Tijera - Juego interactivo (Python 3)
import random

VALIDAS = {'piedra', 'papel', 'tijera'}
ALIASES = {'r': 'piedra', 'p': 'papel', 't': 'tijera'}

def normalizar(entrada):
    s = entrada.strip().lower()
    if s in VALIDAS: return s
    if s in ALIASES: return ALIASES[s]
    return None

def decidir_ganador(player, comp):
    if player == comp: return 'empate'
    if (player == 'piedra' and comp == 'tijera') or \
       (player == 'tijera' and comp == 'papel') or \
       (player == 'papel' and comp == 'piedra'):
        return 'jugador'
    return 'computadora'

def eleccion_cpu():
    return random.choice(list(VALIDAS))

def jugar_ronda():
    while True:
        entrada = input("Elige (piedra/papel/tijera) o (r/p/t): ")
        elec = normalizar(entrada)
        if elec is None:
            print("Entrada no válida. Intenta 'piedra', 'papel', 'tijera' o 'r/p/t'.")
            continue
        comp = eleccion_cpu()
        res = decidir_ganador(elec, comp)
        print(f"Tú: {elec}  —  CPU: {comp}")
        if res == 'empate':
            print("Resultado: Empate.")
        elif res == 'jugador':
            print("Resultado: ¡Ganaste la ronda!")
        else:
            print("Resultado: Gana la computadora.")
        return res

def mejor_de(n):
    objetivo = n//2 + 1
    marcador = {'jugador':0,'computadora':0,'empate':0}
    ronda = 1
    while marcador['jugador'] < objetivo and marcador['computadora'] < objetivo:
        print(f"\n--- Ronda {ronda} ---")
        r = jugar_ronda()
        marcador[r] += 1
        print(f"Marcador -> Tú: {marcador['jugador']}  CPU: {marcador['computadora']}  Empates: {marcador['empate']}")
        ronda += 1
    ganador = "TÚ" if marcador['jugador'] > marcador['computadora'] else "COMPUTADORA"
    print(f"\nGanador del mejor de {n}: {ganador}")
    return marcador

def infinito():
    marcador = {'jugador':0,'computadora':0,'empate':0}
    ronda = 1
    while True:
        print(f"\n--- Ronda {ronda} ---")
        r = jugar_ronda()
        marcador[r] += 1
        print(f"Marcador -> Tú: {marcador['jugador']}  CPU: {marcador['computadora']}  Empates: {marcador['empate']}")
        seguir = input("¿Otra ronda? (s/n): ").strip().lower()
        if seguir not in ('s','si','y','yes'): break
        ronda += 1
    print("\nResultado final:")
    print(f"Tú: {marcador['jugador']}  CPU: {marcador['computadora']}  Empates: {marcador['empate']}")
    return marcador

def main():
    print("=== Piedra, Papel o Tijera ===")
    modo = input("Selecciona modo: 1) Infinito  2) Mejor de N  (1/2): ").strip()
    if modo == '2':
        while True:
            n = input("Introduce N (impar, ej. 3,5,7): ").strip()
            if not n.isdigit() or int(n) <= 0 or int(n) % 2 == 0:
                print("N debe ser un entero positivo impar.")
                continue
            mejor_de(int(n))
            break
    else:
        infinito()

if __name__ == "__main__":
    main()


