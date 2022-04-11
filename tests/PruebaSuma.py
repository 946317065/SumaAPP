import unittest
from src.logica.Suma import Suma

class PruebaSuma (unittest.TestCase):
    def setUp(self):
        self.suma = Suma ()

    def tearDown(self):
        self.suma=None

    def test_operacionSuma_dosNumerosPositivos_retornaSuma(self):
        #Arrage
        self.sumando1=9
        self.sumando2=4
        self.resultadoesperado=13

        #DO
        self.resultadoActual=self.suma.operacionSuma(self.sumando1,self.sumando2)


        # Assert
        self.assertEquals(self.resultadoesperado,self.resultadoActual)

    def test_operacionSuma_dosNumerosNegativos_retornaSuma(self):
        #Arrage
        self.sumando1=-3
        self.sumando2=-7
        self.resultadoesperado=-10

        #DO
        self.resultadoActual=self.suma.operacionSuma(self.sumando1,self.sumando2)


        # Assert
        self.assertEquals(self.resultadoesperado,self.resultadoActual)




