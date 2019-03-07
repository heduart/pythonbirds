from unittest import TestCase
from oo.carro import Motor

class CarroTestCase(TestCase):
    def test_velocidade_inicial(self):
        motor = Motor()
        # Colocar o valor esperado como primeiro em seguida o valor efetivo que será recebido.
        self.assertEqual(0, motor.velocidade)



