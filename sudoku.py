
class sudok():

    def __init__(self, tablero):


        self.tablero = [[0 for __ in range(9)] for _ in range(9)]

        self.tableroV = tablero


        i = -1

        j = -1

        for fila in self.tableroV:

             i += 1

             j = -1

             for valor in fila:

                j += 1

                if valor.isdigit():

                    self.tablero[i][j] = valor

                if valor == 'x':

                    self.tablero[i][j] = valor


        self.tableroV = self.tablero

    def recorrer_fyc(self, num, i, j):

        for columna in range (0,9):
            if num == self.tablero[i][columna]:
                return False

        for fila in range (0,9):
            if num == self.tablero[fila][j]:
                return False
        
        return True


    def bloques(self, num, fila, columna):

        if (fila < 3):

            fila = 0

        elif (fila >= 3 and fila <= 5):

            fila = 3

        else:

            fila = 6

        if (columna < 3):

            columna = 0

        elif (columna >= 3 and columna <= 5):

            columna = 3

        else:

            columna = 6

        for i in range(3):
            
            for j in range(3):

                if self.tablero[fila + i][columna + j] == num:

                    return False

        return True

    def tablerox(self, i, j):
        if "x" == self.tableroV[i][j]:
            return True
        
        return False

    def ganar(self):
        for columna in range (0,9):
            for fila in range (0,9):
                if "x" == self.tablero[fila][columna]:
                    return False

        return True

    def ingresarnum(self,num, x ,y ): 
        if self.ganar() == True:
            return 'ganaste'

        if self.tablerox(x, y) == True:
            if self.recorrer_fyc(num, x ,y) == True:
                if self.bloques(num, x, y) == True:
                    self.tablero[x][y] = num
                    return "numero ingresado"
                else:
                    return "ingrese otro numero"
            else:
                return "ingrese otro numero"
        else:
            return "coordenada equivocada"  





        


       
        
        




        