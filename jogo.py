# Personagem: classe mae
# Heroi: controlado pelo usuario 
# Inimigo: adversario do usuario

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

        def get_nome(self):
            return self.__nome
        
        def get_vida(self):
            return self.__vida
        
        def get_nivel(self):
            return self.__nivel
        
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

        def get_habilidade(self):
            return self.__habilidade