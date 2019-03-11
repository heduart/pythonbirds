# import sklearn

"""Você deve criar uma classe carro que vai possuir dois atributos compostos para outras duas classes.

1) Motor – O motor terá a responsabilidade de controlar a velocidade. Ele oferece os seguintes atributos
(lembrar que tudo é atributos).
    1 – Atributo de dado velocidade.
    2 – Método acelerar, que deverá incrementar a velocidade de uma unidade.
    3 – Método frear que deverá decrementar a velocidade de duas unidades.

2) Direção – Terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos.
    1 – Valor de direção com os seguintes atributos: Norte, Su, Leste e Oeste.
    2 – Método girar_a_direita()
    3 – Método girar_a_esquerda()

   N
O     L
   S

    Exemplo:
    # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    >>> # Testando a direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'

    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0

    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1

    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""
norte='direcao'

class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    # No caso da velocidade o carro não se preocupa com calcular a velocidade, é delegado esse trabalho para
    # por isso é uma composição.
    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()


NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Direcao:

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        if self.valor == NORTE:
            self.valor = LESTE
        elif self.valor == LESTE:
            self.valor = SUL
        elif self.valor == SUL:
            self.valor = OESTE
        elif self.valor == OESTE:
            self.valor = NORTE

    def girar_a_esquerda(self):
        if self.valor == NORTE:
            self.valor = OESTE
        elif self.valor == OESTE:
            self.valor = SUL
        elif self.valor == SUL:
            self.valor = LESTE
        elif self.valor == LESTE:
            self.valor = NORTE


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


# if __name__ == '__main__':
#     # Testando motor
#     motor = Motor()
#     print(f'Verificando a velocidade: {motor.velocidade}')
#     # 0
#
#     motor.acelerar()
#     print(motor.velocidade)
#     # 1
#
#     motor.acelerar()
#     print(motor.velocidade)
#     # 2
#     motor.acelerar()
#     print(motor.velocidade)
#     # 3
#     motor.frear()
#     print(motor.velocidade)
#     # 1
#     motor.frear()
#     print(motor.velocidade)
#     # 0
#
#     print(f'\033[1:45mApresentando a direção do veículo: \033[m\n')
#     # >>>testando.direção
#     direcao = Direcao()
#     print(direcao.valor)
#     # ‘Norte’
#     direcao.girar_a_direita()
#     print(direcao.valor)
#     # ‘Sul’
#     direcao.girar_a_direita()
#     print(direcao.valor)
#     # ‘Oeste’
#     direcao.girar_a_direita()
#     print(direcao.valor)
#     # ‘Norte’
#     direcao.girar_a_esquerda()
#     print(direcao.valor)
#     # ‘Sul’
#     direcao.girar_a_esquerda()
#     print(direcao.valor)
#     # 'Leste'
#     direcao.girar_a_esquerda()
#     print(direcao.valor)
#     # ‘Norte’
#
#     carro = Carro(direcao, motor)
#     print(carro.calcular_velocidade())
#     # 0
#     carro.acelerar()
#     print(carro.calcular_velocidade())
#     # 1
#     carro.acelerar()
#     print(carro.calcular_velocidade())
#     # 2
#     carro.frear()
#     print(carro.calcular_velocidade())
#     # 0
#     carro.calcular_direcao()
#     print(carro.calcular_direcao())
#     # ‘Norte’
#     carro.girar_a_direita()
#     print(carro.calcular_direcao())
#     # ‘Leste’
#     carro.girar_a_esquerda()
#     print(carro.calcular_direcao())
#     # ‘Norte’
#     carro.girar_a_esquerda()
#     print(carro.calcular_direcao())
#     # ‘Oeste’
