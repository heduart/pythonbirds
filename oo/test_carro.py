from unittest import TestCase
from oo.carro import Motor
from oo.carro import Direcao


class CarroTestCase(TestCase):
    def test_velocidade_inicial(self):
        motor = Motor()
        # Colocar o valor esperado como primeiro em seguida o valor efetivo que será recebido.
        self.assertEqual(0, motor.velocidade)

    def test_acelerar(self):
        motor = Motor()
        # Como estamos verificando o retorno após acelerar o veículo é de uma unidade é necessário acelerar e
        # verificar se o retorno foi correspondido, para isso chamar .
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
        motor.acelerar()
        self.assertEqual(2, motor.velocidade)
        motor.acelerar()
        self.assertEqual(3, motor.velocidade)

    def test_frear(self):
        motor = Motor()
        motor.acelerar()
        motor.acelerar()
        motor.acelerar()
        motor.frear()
        self.assertEqual(1, motor.velocidade)
        motor.frear()
        self.assertEqual(0, motor.velocidade)

    def test_calcular_direcao(self):
        direcao = Direcao()
        self.assertEqual('Norte', direcao.valor)
