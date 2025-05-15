import json
import tabulate

while True:
    print('-'*30)
    print('\033[1;32mBEM-VINDO, O QUE DESEJA FAZER?\033[m')
    print('-'*30)
    pergunta_1 = input('1- Fazer cadastro \n2- Fazer login \n3- Sair \nResposta:').strip()
    

    match pergunta_1:

        case '1':
             while True:
                with open('usuarios.txt', 'a+') as arquivo_txt:
                    print('-'*40)
                    print('Para realizar o cadastro informe')
                    try:
                        usuario = input('Nome de usuario: ').strip()
                        senha = int(input('informe uma senha(apenas numeros): '))
                        id_usuario = f'{usuario},{senha} \n'

                    except:
                        print('-'*40)
                        print('ERRO, TENTE NOVAMENTE')
                        continue

                    arquivo_txt.seek(0)
                    usuarios_txt = arquivo_txt.readlines()

                    if id_usuario not in usuarios_txt:
                        arquivo_txt.write(id_usuario)
                        print('-'*40)
                        print('CADASTRO REALIZADO')
                        print('-'*40)
                    
                    else:
                        print('-'*40)
                        print('Usuario ou senha existentes, tente novamente')
                        continue
                break


        case '2':
            while True:
                with open('usuarios.txt', 'r') as arquio_txt:
                    print('-'*40)
                    print('Para realizar o login informe')

                    try:
                        usuario = input('O seu nome de usuário: ').strip()
                        senha = int(input('informe a sua senha(apenas números): '))
                        id_usuario = f'{usuario},{senha} \n'

                    except:
                        print('-'*40)
                        print('ERRO, TENTE NOVAMENTE')
                        continue

                    arquio_txt.seek(0)

                    usuarios_txt = arquio_txt.readlines()

                    if id_usuario not in usuarios_txt:
                        print('-'*40)
                        print('Usuário não encontrado, tente novamente')
                        
                        continue

                    else:
                        print('-'*40)
                        print('Login realizado')
                        print('-'*40)

                        while True:
                            pergunta_2 = input('informe qual ação deseja realizar \n1- Adicionar atividade \n2- Visualizar atividade \n3- Editar atividade \n4- Excluir atividade \n5- Sair para o menu \nResposta: ').strip()

                            match pergunta_2:

                                case '1':
                                    with open('atividades.json', 'a') as atividades:

                                        print('-'*40)

                                        print('Para realizar o cadastro da atividade informe: ') 

                                        titulo_atividade = input('Titulo: ').lower().strip()

                                        descricao = input('Descrição: ').lower().strip()

                                        data_inicio = input('Data de Inicio: ').lower().strip()

                                        data_final = input('Data final: ').lower().strip()

                                        horario_estudar = input('Horário previsto para estudar essa atividade: ').lower().strip()

                                        prioridade = input('Prioridade dessa atividade: ').lower().strip()


                                        dicionario_atividades = {
                                            id_usuario: {
                                                titulo_atividade: {
                                                    'descrição': descricao,
                                                    'data de inicio': data_inicio,
                                                    'data final': data_final,
                                                    'horario de estudar': horario_estudar,
                                                    'prioridade': prioridade

                                                }
                                            }
                                        }

                                        
                                        dicionario_json = json.dumps(dicionario_atividades) + '\n'

                                        atividades.write(dicionario_json)
                                        
                                        print('-'*40)
                                        print('Atividade Adicionada')
                                        print('-'*40)


                                case '2':
                                    with open('atividades.json', 'r') as atividades:
                                        titulo_registrado = input('Título da atividade: ').lower().strip()
                                        dicionario_py = json.load(atividades)


                                        for elementos in dicionario_py[id_usuario].items():

                                            if titulo_registrado in elementos:
                                                lista = list(dicionario_py[id_usuario][titulo_registrado].items())
                                                tabela = tabulate.tabulate(lista)
                                                print(tabela)
                                            
                                            else:
                                                print('-'*30)
                                                print('Atividade não encontrada')
                                                print('-'*30)
                                                                                       
                                case '3':
                                    with open('atividades.json', 'r+') as atividades:
                                        print('Para editar uma atividade informe:')

                                        titulo_registrado = input('Título da atividade: ').lower().strip()

                                        dicionario_py = json.load(atividades)

                                        
                                        for elementos in dicionario_py[id_usuario].items():
                                            
                                            if titulo_registrado in elementos:

                                                dicionario_py[id_usuario][titulo_registrado]['descrição'] = input('Nova descrição: ').lower().strip()

                                                dicionario_py[id_usuario][titulo_registrado]['data de inicio'] = input('Nova data de início: ').lower().strip()

                                                dicionario_py[id_usuario][titulo_registrado]['data final'] = input('Nova data final: ').lower().strip()

                                                dicionario_py[id_usuario][titulo_registrado]['horario de estudar'] = input('Novo horário de estudar: ').lower().strip()

                                                dicionario_py[id_usuario][titulo_registrado]['prioridade'] = input('Nova prioridade: ').lower().strip()

                                                with open('atividades.json', 'w') as atividades:

                                                    novo_dicionario_json = json.dumps(dicionario_py) + '\n'

                                                    atividades.write(novo_dicionario_json)
                                                    print('-'*30)
                                                    print('Atividade modificada com sucesso')
                                                    print('-'*30)


                                            else:
                                                print('-'*30)
                                                print('Atividade não encontrada')
                                                print('-'*30)


                                case '4':
                                    with open('atividades.json', 'r') as atividades:
                                        print('Para excluir uma atividade informe: ')
                                        titulo_registrado = input('Título da atividade: ').lower().strip()

                                        dicionario_py = json.load(atividades)

                                        if titulo_registrado in dicionario_py[id_usuario]:
                                            with open('atividades.json', 'w') as atividades:
                                                dicionario_py.clear()
                                                dicionario_json = json.dumps(dicionario_py)
                                                atividades.write(dicionario_json + '\n')

                                                print('-'*30)
                                                print('Atividade removida')
                                                print('-'*30)

                                        else:
                                            print('-'*30)
                                            print('Atividade não encontrada')
                                            print('-'*30)
                                            
                                case '5':
                                    break
                                            
                                        
                                                                                    

                    break


        
        case '3':
            print('-'*40)
            print('FINALIZADO')
            print('-'*40)
            break


    