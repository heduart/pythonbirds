# O termo classe também pode ser utilizada como sinônimo de tipo.

class Pessoa:
    # Criando um atributo de classe, utilizado para economizar memória quando um determinado dado é comum
    # para várias instâncias criadas.
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    herbert = Pessoa(nome='Herbert', idade=39)
    ana = Pessoa(nome='Ana', idade=20)
    # Passando o objeto herbert e ana como atributo para o objeto luciano, indicando o filho
    luciano = Pessoa(herbert, ana, nome='Luciano', idade=63)
    # Forma errada de chamar a classe, passando p sem necessidade

    print(Pessoa.cumprimentar(luciano))
    # Confirmando o endereço de memória criado.
    print(id(luciano))
    # p é passado implicitamente pelo python referenciando o endereço de memória.
    print(luciano.cumprimentar())

    print(f'Nome: {luciano.nome}, {luciano.idade} anos.')


    # Como pode ser criado mais de um filho para luciano, por se um objeto complexo para impressão dos filhos
    # é necessário criar um looping para aptresentar cada filho de luciano.
    print(f'Representação do objeto filho: {luciano.filhos}')
    for filho in luciano.filhos:
        print(f'{filho.nome} é filho(a) de {luciano.nome} ')

    # Atrinuindo um valor para o atributo de classe nome.
    print(f'\033[1;34mFazendo o teste com o atributo de classe nome: \033[1;31m{herbert.nome}.\033[m')

    # Atributos dinâmicos: Python permite a criação de atributos em tempo de execução (não é uma boa prática),
    # mas pode ser feito.

    luciano.sobrenome = 'Ramalho'
    # Imprimindo o atributo dinâmico para teste, esse atributo não aparece para os demais objetos criados.
    print(f'Atributo: {luciano.nome}, atributo dinâmico: {luciano.sobrenome}')
    print(f'__dict__ de Luciano: {luciano.__dict__}')
    print(f'__dict__ de Herbert: {herbert.__dict__}')

    # Também podemos remover atributos dinamicamente, no exemplo é possível verificar que os filhos não
    # aparecem mais.
    del luciano.filhos
    print(f'Atributos filhos removido dinamicamente: {luciano.__dict__}')

    # Imprimindo o atributo de classe criado para compartilhar o mesmo dados pelas instâncias.
    print(f'\n{herbert.nome}, olhos: {herbert.olhos} - Memória: {id(herbert.olhos)}\n{herbert.__dict__}')
    print(f'{luciano.nome}, olhos: {luciano.olhos} - Memória: {id(herbert.olhos)}\n{luciano.__dict__}')


    # Alterando o atributo de classe para um determinado objeto, nesse a alteração é feita somente para o
    # atributo de classe do luciano.
    luciano.olhos = 1
    print(f'\n{luciano.nome}, olhos: {luciano.olhos} - Memória: {id(herbert.olhos)}\n{luciano.__dict__}')

    # Podemos também fazer uma alteração para o atributo de classe diretamente, dessa forma todas as novas
    # instâncias sofrerão alteração quando utilizar o atributo.
    Pessoa.olhos = 3
    print(f'\n{herbert.nome}, olhos: {herbert.olhos} - Memória: {id(herbert.olhos)}\n{herbert.__dict__}')
    print(f'{luciano.nome}, olhos: {luciano.olhos} - Memória: {id(herbert.olhos)}\n{luciano.__dict__}')
