# O termo classe também pode ser utilizada como sinônimo de tipo.

class Pessoa:

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    # Forma errada de chamar a classe, passando p sem necessidade
    print(Pessoa.cumprimentar(p))
    # Confirmando o endereço de memória criado.
    print(id(p))
    # p é passado implicitamente pelo python referenciando o endereço de memória.
    print(p.cumprimentar())
