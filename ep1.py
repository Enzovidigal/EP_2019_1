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
        "na entrada do Insper, e quer procurar o professor para pedir um"
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

        # Feature 1 e Feature 2: Monstros e combate. Tambem inauguramos o inventário, se o monstro for derrotado.

        tem_monstro = random.randint(1, 3)
        tem_premio = random.randint(1,8)
        batalha = False
        if tem_monstro==1:
            vida_monstro=3
            print('\nGRRRR!!! VOCÊ DEU DE CARA COM UM MONSTRO, LUTE CONTRA ELE')

            luta_ou_foge = input("\nVocê tem {0} vidas, e o monstro tem {1}, quer lutar ou fugir?".format(hitpoints, vida_monstro))
            if luta_ou_foge=='lutar' or luta_ou_foge=='fugir':
                batalha=True
            else:
                print('nem lutar nem fugir? O monstro nao te entendeu... Mas te comeu')
                game_over=True
                break
            
            while batalha:
                if "espada" in inventario:
                    print("Vc tem a espada pirocuda, vc derrotou o monstro")
                    break
                else:
                    if luta_ou_foge=='lutar':
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
                            print("\n\nVc derrotou o monstro, ganhou um prêmio\nAgora tens a chave para entrar na salinha de estudos!")                    
                            inventario.append('Chave1')       
                            break
                        elif vida_monstro == 0 and 'Chave1' in inventario:
                            print("Vc derrotou o monstro")
                            break

                        
                        luta_ou_foge = input("Você tem {0} vidas e o monstro tem {1}, quer lutar ou fugir?".format(hitpoints, vida_monstro))

                    if luta_ou_foge=='fugir':  
                        x=random.randint(1,2)
                        if x==2:
                            print('O monstro não deixou vc fugir! perdeu 1 vida!')
                            hitpoints-=1
                            if hitpoints!=0:
                                luta_ou_foge=input("Você tem {0} vidas, quer lutar ou tentar fugir denovo?".format(hitpoints))
                            if hitpoints == 0:
                                print("\n\nO MONSTRO TE DERROTOU")
                                game_over = True
                                break
                        else:
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

        #Feature 3: Aqui estão os itens que o player ganha ao tomar certas decisões ou os itens que ele precisa ter para entrar em um novo cenario
       
        #*o que o usuario ganha se for no saboroso
        if nome_cenario_atual=='saboroso':
            print("Você recarregou suas energias. Agora você tem 3 vidas novamente")
            hitpoints = 3
        
        #*condicao para o player entrar na salinha
        if nome_cenario_atual=='salinha de estudos' and "Chave1" not in inventario:
            print("Oh Oh... vc ainda não tem a chave para abrir a salinha! Derrote o monstro primeiro")
            nome_cenario_atual = 'biblioteca' 
            cenario_atual = cenarios[nome_cenario_atual] 
        elif nome_cenario_atual=='salinha de estudos' and "Chave1" in inventario:
            print("AE CACHORRO, VC CONSEGUIU O QR CODE PARA ENTRAR NO PREDIO NOVO")
            inventario.append("qr code")   

        #*condicao para o player entrar no predio novo
        if nome_cenario_atual=='predio novo' and 'qr code' not in inventario: 
            print("Oh Oh... vc ainda não tem o Qr code para entar no predio novo! Entre na salinha de estudos primeiro")
            nome_cenario_atual = 'inicio' 
            cenario_atual = cenarios[nome_cenario_atual]
        
        #*condicao para o player encontrar o professor no lado de fora do sexto andar
        if nome_cenario_atual=="lado fora" and "Chave2" not in inventario:
            print("Oh Oh... vc ainda não tem a chave para encontrar o professor! Va no Fablab primeiro")
            nome_cenario_atual = 'sexto andar' 
            cenario_atual = cenarios[nome_cenario_atual]
        elif nome_cenario_atual=="lado fora" and "Chave2" in inventario:
            cenario_atual = cenarios[nome_cenario_atual]
            break
            

        
        #*O que o player ganha se for no fablab
        deu_ruim = random.randint(1,5)

        #**fresadora
        if nome_cenario_atual=="fresadora":
            print("Você nao soube usar a fresadora e se machucou!")
            break
        #**cortadora laser
        if nome_cenario_atual=="cortadora laser" and deu_ruim==1:
            print("Voce nao soube usar a cortadora e se machuchou")
            hitpoints = 0
            break
        elif nome_cenario_atual=="cortadora laser" and deu_ruim!=1:
            print("Pronto! Agora sera mais facil derrotar o monstro da proxima vez")
            inventario.append("espada")
            nome_cenario_atual="fablab"
            cenario_atual = cenarios[nome_cenario_atual]
        
        #**impressora 3d
        if nome_cenario_atual=="impressora 3d" and deu_ruim==1:
            print("Voce nao soube usar a impressora e se machuchou")
            hitpoints = 0
            break
        elif nome_cenario_atual=="impressora 3d" and deu_ruim!=1:
            print("Pronto! Agora voce pode abrir a porta que te leva ao professor")
            inventario.append("Chave2")
            nome_cenario_atual="fablab"
            cenario_atual = cenarios[nome_cenario_atual]
        
        
###########################################################
        # Aqui mostramos ao player as opcões que podem ser tomadas e o titulo e descricao do capitulo.
        # dependendo da escolha do jogador, o "próximo cenario atual" será igual ao que ele escolheu.

        print('\n\n')
        print(cenario_atual['titulo'])
        print('-'*(len(cenario_atual['titulo'])))
        print('\n')
        print(cenario_atual['descricao'])



        opcoes = cenario_atual['opcoes']
        #  Feature 4: Teletransporte
        tem_teletransporte = random.randint(1,10)
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        elif tem_teletransporte==2:
            pergunta_teletransporte = input("Você ganhou um teletransporte! Para que cenario do jogo deseja ir? ")
            if pergunta_teletransporte in cenarios:
                nome_cenario_atual = pergunta_teletransporte
            else:
                print('Vc entrou no teletrasnporte e caiu em um loop sem saida')
                game_over = True
                break
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
        
        

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
