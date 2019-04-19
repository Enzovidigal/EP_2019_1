# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno B: Enzo Vidigal, enzolv@al.insper.edu.br
# - aluno A: Joao Zsigmond, joaoz@al.insper.edu.br
import random
import json
import sys

def carregar_cenarios():
    with open('cenarios.txt', 'r') as episodios:
        cenarios_dict = json.load(episodios)
        cenarios = cenarios_dict
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
    
    inventario = []

    while not game_over:
        
        tem_monstro = random.randint(1, 5)
        tem_premio = random.randint(1,8)
        if tem_monstro==1:
            vida_monstro=3
            print('\nGRRRR!!! VOCÊ DEU DE CARA COM UM MONSTRO, LUTE CONTRA ELE')

            luta_ou_foge = input("\nVocê tem {0} vidas, e o monstro tem {1}, quer lutar ou fugir?".format(hitpoints, vida_monstro))
            while luta_ou_foge!='fugir':
                prob = random.randint(1,5)
                
                if prob==1 or prob==2:
                    print('O monstro ganhou o ataque, perde 1 vida')
                    hitpoints-=1
                else:
                    print('Vc ganhou o ataque o monstro perdeu 1 vida')
                    vida_monstro-=1
                
                if hitpoints == 0:
                    print("\n\nO MONSTRO TE DERROTOU")
                    game_over = True
                    break
                elif vida_monstro == 0 and 'Chave1' not in inventario:
                    print("\n\nVc derrotou o monstro, ganhou um prêmio\nAgora tens a chave para passar para entrar na sala do mago!")                    
                    inventario.append('Chave1')       
                    break
                
                luta_ou_foge = input("Você tem {0} vidas e o monstro tem {1}, quer lutar ou fugir?".format(hitpoints, vida_monstro))
                x=random.randint(1,3)
                if luta_ou_foge=='fugir':  
                    if x!=2:
                        print('O monstro não deixou vc fugir! perdeu 1 vida!')
                        hitpoints-=1
                        luta_ou_foge=input("Você tem {0} vidas, quer lutar ou tentar fugir denovo?".format(hitpoints))
                        if hitpoints == 0:
                            print("\n\nO MONSTRO TE DERROTOU")
                            game_over = True
                            break
               
            if game_over==True:
                break
            elif luta_ou_foge=='fugir':
                print('voce fugiu com segurança')
            cenario_atual = cenarios[nome_cenario_atual]

            
        elif tem_premio==1:
            print('\nPARABÉNS, VOCÊ GANHOU UMA VIDA')
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
                print('\n')
            escolha = input('Escolha sua opção: ')

            if escolha in opcoes:
                nome_cenario_atual = escolha
            elif hitpoints == 0:
                game_over = True
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

        #adicionando items ao inventário
        if  nome_cenario_atual == 'andar professor':
            print("\n\nBoua! Você ganhou uma espada")
            inventario.append('espada')



    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
