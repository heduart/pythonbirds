# O termo classe também pode ser utilizada como sinônimo de tipo.

class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Luciano')
    # Forma errada de chamar a classe, passando p sem necessidade
    print(Pessoa.cumprimentar(p))
    # Confirmando o endereço de memória criado.
    print(id(p))
    # p é passado implicitamente pelo python referenciando o endereço de memória.
    print(p.cumprimentar())
    # Atrinuindo um valor para o atributo de classe nome.
    p.nome = 'Herbert'
    p.idade = 39
    print(f'\033[1;34mfazendo o teste com o atributo de classe nome: \033[1;31m{p.nome}.\033[m')
