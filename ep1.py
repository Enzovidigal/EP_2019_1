# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno B: Enzo Vidigal, enzolv@al.insper.edu.br
# - aluno A: Joao Zsigmond, joaoz@al.insper.edu.br
import random
import sys

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    
    with open('monster.txt', 'r') as monster:
            monster = monster.read()
            print(monster)

    hitpoints=3

    while not game_over:
        tem_monstro = random.randint(1, 5)
        tem_premio = random.randint(1,8)
        if tem_monstro==2:
            print('\nUM MONSTRO TE MORDEU FILHÃO, LUTE CONTRA ELE')

            luta_ou_foge = input("Você tem {0} vidas, quer lutar ou fugir?".format(hitpoints))
            while luta_ou_foge=='l' and not game_over:
                probabilidade = random.randint(1,5)
                if probabilidade==1:
                    resultado_combate = 1
                else:
                    resultado_combate = -1
                hitpoints = hitpoints + resultado_combate
                if hitpoints == 0:
                    print("\n\nVC morreu para o mostro")
                    sys.exit()
                    game_over = True
                luta_ou_foge = input("Você tem {0} vidas, quer lutar ou fugir?".format(hitpoints))
                
           
            if luta_ou_foge=='fugir':
                cenario_atual = cenarios[nome_cenario_atual]



            
        elif tem_premio==1:
            print('\nPARABÉNS AMIGO, VOCÊ GANHOU UMA VIDA')
            hitpoints+=1
        print('\n')
        print("###---###---###    Você ainda tem {0} vida(s)    ###---###---###".format(hitpoints))
        cenario_atual = cenarios[nome_cenario_atual]

###########################################################
        
        print('\n\n')
        print(cenario_atual['titulo'])
        print('-'*(len(cenario_atual['titulo'])))
        print('\n')
        print(cenario_atual['descricao'])



        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print('O que voce quer fazer? \n')
            for key, value in opcoes.items():
                print('{0} : {1}'. format(key, value))
            escolha = input('Escolha sua opção: ')

            if escolha in opcoes:
                nome_cenario_atual = escolha
            elif hitpoints == 0:
                game_over = True
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True


    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
