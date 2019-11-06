import unittest
from sudoku import sudok
from parameterized import parameterized

class TestSudoku(unittest.TestCase):

    def setUp(self):

        self.juego = sudok([

            '53xx7xxxx',

            '6xx195xxx',

            'x98xxxx6x',

            '8xxx6xxx3',

            '4xx8x3xx1',

            '7xxx2xxx6',

            'x6xxxx28x',

            'xxx419xx5',

            'xxxx8xx79'

        ])


    def test_columna(self):
        self.assertEqual(self.juego.ingresarnum('8',0,3), "ingrese otro numero")
        self.assertEqual(self.juego.tablero,
            [['5', '3', 'x', 'x', '7', 'x', 'x', 'x', 'x'],
            ['6', 'x', 'x', '1', '9', '5', 'x', 'x', 'x'],
            ['x', '9', '8', 'x', 'x', 'x', 'x', '6', 'x'],
            ['8', 'x', 'x', 'x', '6', 'x', 'x', 'x', '3'],
            ['4', 'x', 'x', '8', 'x', '3', 'x', 'x', '1'],
            ['7', 'x', 'x', 'x', '2', 'x', 'x', 'x', '6'],
            ['x', '6', 'x', 'x', 'x', 'x', '2', '8', 'x'],
            ['x', 'x', 'x', '4', '1', '9', 'x', 'x', '5'],
            ['x', 'x', 'x', 'x', '8', 'x', 'x', '7', '9']])
   
    def test_fila(self):
        self.assertEqual(self.juego.ingresarnum('7',5,3),"ingrese otro numero")    
        self.assertEqual(self.juego.tablero,
          [['5', '3', 'x', 'x', '7', 'x', 'x', 'x', 'x'],
           ['6', 'x', 'x', '1', '9', '5', 'x', 'x', 'x'],
           ['x', '9', '8', 'x', 'x', 'x', 'x', '6', 'x'],
           ['8', 'x', 'x', 'x', '6', 'x', 'x', 'x', '3'],
           ['4', 'x', 'x', '8', 'x', '3', 'x', 'x', '1'],
           ['7', 'x', 'x', 'x', '2', 'x', 'x', 'x', '6'],
           ['x', '6', 'x', 'x', 'x', 'x', '2', '8', 'x'],
           ['x', 'x', 'x', '4', '1', '9', 'x', 'x', '5'],
           ['x', 'x', 'x', 'x', '8', 'x', 'x', '7', '9']])
    
    def test_bloques(self):
        self.assertEqual(self.juego.ingresarnum('6',0,2),"ingrese otro numero")    
        self.assertEqual(self.juego.tablero,
          [['5', '3', 'x', 'x', '7', 'x', 'x', 'x', 'x'],
           ['6', 'x', 'x', '1', '9', '5', 'x', 'x', 'x'],
           ['x', '9', '8', 'x', 'x', 'x', 'x', '6', 'x'],
           ['8', 'x', 'x', 'x', '6', 'x', 'x', 'x', '3'],
           ['4', 'x', 'x', '8', 'x', '3', 'x', 'x', '1'],
           ['7', 'x', 'x', 'x', '2', 'x', 'x', 'x', '6'],
           ['x', '6', 'x', 'x', 'x', 'x', '2', '8', 'x'],
           ['x', 'x', 'x', '4', '1', '9', 'x', 'x', '5'],
           ['x', 'x', 'x', 'x', '8', 'x', 'x', '7', '9']])
    
    
    def test_tablerox(self):
        self.assertEqual(self.juego.ingresarnum('4',1,0),"coordenada equivocada")    
        self.assertEqual(self.juego.tablero, 
           [['5', '3', 'x', 'x', '7', 'x', 'x', 'x', 'x'],
           ['6', 'x', 'x', '1', '9', '5', 'x', 'x', 'x'],
           ['x', '9', '8', 'x', 'x', 'x', 'x', '6', 'x'],
           ['8', 'x', 'x', 'x', '6', 'x', 'x', 'x', '3'],
           ['4', 'x', 'x', '8', 'x', '3', 'x', 'x', '1'],
           ['7', 'x', 'x', 'x', '2', 'x', 'x', 'x', '6'],
           ['x', '6', 'x', 'x', 'x', 'x', '2', '8', 'x'],
           ['x', 'x', 'x', '4', '1', '9', 'x', 'x', '5'],
           ['x', 'x', 'x', 'x', '8', 'x', 'x', '7', '9']])
    
    def test_ganar(self):
       self.juego = sudok([
           '531171111',
           '611195111',
           '198111161',
           '811161113',
           '411813111',
           '711121116',
           '161111281',
           '111419115',
           '11118117x'
          ])
       self.assertEqual("numero ingresado",self.juego.ingresarnum('4', 8, 8)) 
       self.assertTrue(self.juego.ganar()) 

    @parameterized.expand([
    ('6',0,2),('5',2,3),
    ('2',0,3),('3',6,0),
    ('1',8,0),('4',8,8),
    ('2',0,8),('3',7,0),
    ('4',1,6),('1',3,0)])
    def test_fyc(self,num,f,c):
        self.assertTrue(self.juego.recorrer_fyc(num,f,c))
     
    @parameterized.expand([
    ('1',0,2),('4',0,3),
    ('4',6,0),('3',6,2),
    ('4',6,0),('2',0,2),
    ('3',0,6),('1',8,0),
    ('1',8,8),('2',8,2)])
    def test_numero_en_bloque_correcto(self,num,f,c):
        self.assertTrue(self.juego.bloques(num,f,c))
   
    @parameterized.expand([
    ('6',0,6), ('5',8,6),
    ('4',8,5),('3',5,3),
    ('1',5,7),('5',0,3),
    ('6',0,8),('3',3,5),
    ('9',2,0),('7',4,1)])
    def test_numero_en_bloque_incorrecto(self, num,f,c):
        self.assertEqual(self.juego.ingresarnum(num,f,c),"ingrese otro numero")

    @parameterized.expand([
    ('7',8,8),('7',0,3),
    ('9',8,0),('4',7,0),
    ('2',5,5),('4',8,3),
    ('4',6,0),('1',0,8),
    ('5',7,7),('3',0,2)])
    def test_fyc(self,num,f,c):
        self.assertFalse(self.juego.recorrer_fyc(num,f,c))
  
    @parameterized.expand([
    (8,0),(0,7),(1,8),(2,0),
    (7,7),(8,1),(6,0),(1,1),
    (0,2),(1,2),(2,8),(7,1),
    (6,2),(1,7),(2,8),(3,1),
    (4,2),(8,3),(1,6),(0,5)])
    def test_posicion_correcta(self,f,c):
        self.assertTrue(self.juego.tablerox(f,c))
  

        

    







          

       
    


        




if __name__ == "__main__":

    unittest.main()



