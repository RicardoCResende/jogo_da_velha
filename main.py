class Impressao:
    def __init__(self):
        self.campos = [1,2,3,4,5,6,7,8,9]
        print('#' * 40)
        print('     BEM VINDO JOGADOR\n  ESTE É O JOGO DA VELHA!!!')
        print('#' * 40)

    def imprimir(self, teste=False):
        print('')
        print(f'   {self.campos[0]} | {self.campos[1]} | {self.campos[2]}')
        print('  ---|---|---')
        print(f'   {self.campos[3]} | {self.campos[4]} | {self.campos[5]}')
        print('  ---|---|---')
        print(f'   {self.campos[6]} | {self.campos[7]} | {self.campos[8]}')
        print('')

    def teste(self):
         for campo, valor in  enumerate(self.campos):
            if campo in (0,3,6):
                if self.campos[campo] == self.campos[campo+1] and self.campos[campo] == self.campos[campo+2]:
                    return True
                    break
            if campo in (0,1,2):
                if self.campos[campo] == self.campos[campo+3] and self.campos[campo] == self.campos[campo+6]:
                    return True
                    break
            if campo in (0, 2):
                if campo == 0:
                    if self.campos[campo] == self.campos[campo+4] and self.campos[campo] == self.campos[campo+8]:
                        return True
                else:
                    if self.campos[campo] == self.campos[campo+2] and self.campos[campo] == self.campos[campo+4]:
                        return True
                 

class Jogador:
    def __init__(self, marca=None):
        if marca == None:
            while True:
                self.marca = input('escolha a sua marca [X ou O]: ').upper()
                if self.marca == 'X' or self.marca == 'O':
                    break
                else:
                    print('Digite x ou o')
                    continue
        else: 
            if marca == 'X':
                self.marca = 'O'
            else:
                self.marca = 'X'
        

class Jogar(Jogador, Impressao):
    def __init__(self):
        Impressao.__init__(self)
        self.jogador1 = Jogador()
        self.jogador2 = Jogador(self.jogador1.marca)

    def jogar(self, marca):
        while True:
            try:
                campo = int(input(f'Jogador {marca} escolha o campo que quer marcar:')) - 1
                if campo == -1:
                    campo = 'q'
                self.campos[campo] = marca
                break
            except:
                print('o numero que digitou não está no tabuleiro')

    def gameplay(self):
        for rodada in range (1, 6):
            teste = self.teste()
            if teste:
                print(f'Jogador {self.jogador2.marca} venceu!!!')
                break
            self.imprimir()
            self.jogar(self.jogador1.marca)
            self.imprimir()
            teste = self.teste()
            if teste:
                print(f'Jogador {self.jogador1.marca} venceu!!!')
                break
            if rodada == 5:
                print('EMPATOU!!!')
                break
            jogo.jogar(self.jogador2.marca)


if __name__ == '__main__':
    
    jogo = Jogar()
    jogo.gameplay()
    