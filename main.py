from pilaHanoi import pila

def getTablero(n):
    tablero = [pila() for i in range(3)]
    for i in range(n,0,-1):
        tablero[0].push(i)
    return tablero

def solve(tablero, n, origen, destino, auxiliar):
    if n == 1:
        disco = tablero[origen].pop()
        tablero[destino].push(disco)
        print(f"D{disco} from T{origen + 1} to T{destino + 1}")
    else:
        solve(tablero, n-1, origen, auxiliar, destino)
        disco = tablero[origen].pop()
        tablero[destino].push(disco)
        print(f"D{disco} from T{origen + 1} to T{destino + 1}")
        solve(tablero, n - 1, auxiliar, destino, origen)

if __name__ == '__main__':
    n = 5
    tablero = getTablero(n)

    print("Tablero de inicio")
    for i, pila in enumerate(tablero):
        print(f"T{i+1}: {pila}")

    print("\nMovimientos a realizar")
    solve(tablero, n, 0, 2, 1)

    print("\nTablero final")
    for i, pila in enumerate(tablero):
        print(f"T{i+1}: {pila}")
