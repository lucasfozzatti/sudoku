import unittest
from interfaz_sudoku import Interfaz



class Test_Interfaz_Sudoku(unittest.TestCase):

    def setUp(self):
        self.int = Interfaz()


    def test_filaocolumna_correcta(self):
        self.assertTrue(self.int.verificar_fyc(2))
    
    def test_filao_columna_incorrecta(self):
        self.assertFalse(self.int.verificar_fyc(32))
   
    def test_numero_correcto(self):
        self.assertTrue(self.int.verificar_entero(4))
    
    def test_numero_incorrecto(self):
        self.assertFalse(self.int.verificar_entero(56))


    


if __name__ == "__main__":
    unittest.main()