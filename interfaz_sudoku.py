
from sudoku import sudok
from api import api


class Interfaz():

    def __init__(self):
        self.Su = sudok(api())

    def verificar_entero(self, n):
        return (0 < n < 10)
           
    def verificar_fyc(self, foc):
        return (0 <= foc < 9)
           

    def Play(self):
        print("         COMIENZA EL JUEGO")
        for i in range(0, 9):
            for j in range(0, 9):
                 print(self.Su.tablero[i][j], end=" | ")
            print(" ")
            
       
        try:
            print("Ingrese fila donde desea poner el numero ( 0 a 8 )")
            f = input(">>")
            if self.verificar_fyc(int(f)) == True:
                print("Ingrese columna donde desea poner el numero ( 0 a 8 )")
                c = input(">>")
                if self.verificar_fyc(int(c)) == True:
                    print("Ingrese numero")
                    n = input(">>")
                    if self.verificar_entero(int(n)) == True:
                        print(self.Su.ingresarnum(n, int(f), int(c)))
                    else:
                        print('Ingrese un numero correcto')
                else:
                    print('Ingrese un numero correcto')
            else:
                print('Ingrese un numero correcto')
        except Exception as w:
            print(w)
            print('Ingrese un numero correcto')

    

juego = Interfaz()

while juego.Su.ganar() == False:
    juego.Play()