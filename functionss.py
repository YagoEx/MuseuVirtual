import os , time
# Login validation function
def login(dictionary):
    while True: # Create a loop for continue showing the login screen until the user enter valid informations 
        print('='*20)
        print('Museu Virtual')
        print('='*20)
        login = input('Login: ')
        password = input('Senha: ')
        
        i = 0
        for item in dictionary:
            if login == item["login"]:
                if password == item["password"]:
                    os.system("cls") # cleans the terminal
                    return item["acess"]
                else:
                    print('Senha incorreta!')
                    time.sleep(2)
                    os.system("cls") # cleans the terminal
                    break
            else:
                i += 1
            if i >= len(dictionary):
                print('Usuário incorreto.')
                time.sleep(2)
                os.system("cls") # cleans the terminal
                break

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista.pop()

    elementos_maiores = []
    elementos_menores = []

    for elemento in lista:
        if elemento > pivot:
            elementos_maiores.append(elemento)
        else:
            elementos_menores.append(elemento)
    return quick_sort(elementos_menores) + [pivot] + quick_sort(elementos_maiores)

def busca_binaria(lista, busca):
    inicio, fim = 0, len(lista)-1

    while inicio <= fim:
        meio = (inicio+fim)//2

        if lista[meio] == busca:
            return meio
        elif lista[meio] < busca:
            inicio = meio + 1
        else:
            fim = meio - 1            
    
    return -1


def gerenciar_usuarios(users):
    while True:
        print("\n1 - Cadastrar Usuários")
        print("2 - Cadastrar Pintor")
        print("3 - Deletar Usuários")
        print("4 - Listar Usuários")
        print("5 - Voltar ao início")

        selecao = input("Selecione uma das opções acima: ")

        try:
            int(selecao)
            if int(selecao) > 5:
                print('Digite somente as opções válidas.')
                continue

        except ValueError:
            print('Digite somente as opções validas.')
            continue
        
        if selecao == "1":
            cadastrar_usuario(users)

        elif selecao == "2":
            deletar = input("\nDigite o usuário que deseja deletar: ")
            deletou = False

            for usuario in users:
                if deletar == usuario["login"]:
                    users.remove(usuario)
                    print("Usuário deletado.")
                    deletou = True
                    break

            if not deletou:
                print('Usuario não encontrado.')
                break

        elif selecao == "3":
            deletar = input("\nDigite o usuário que deseja deletar: ")
            deletou = False

            for usuario in users:
                if deletar == usuario["login"]:
                    users.remove(usuario)
                    print("Usuário deletado.")
                    deletou = True
                    break

            if not deletou:
                print('Usuario não encontrado.')
                break

        elif selecao == "4":
            print("\nLista de Usuários:")
            for usuario in users:
                print(usuario["login"], usuario["acess"])

        elif selecao == "5":
            break

# Cadastrar os usuários
def cadastrar_usuario(users):
    while True:
        print("-"*25)
        print(f'{"Cadastro de usuários":^25}')
        print("-"*25)

        login = input("login: ")
        senha = input("Senha: ")
        acesso = input("Acesso: ")

        for user in users:
            if login == user["login"]:
                print('Usuario já existente.')
                continue

        users.append({"login":login, "password":senha, "acess":acesso})
        print('Usuário cadastrado!')
        criar_log(users, login)
        break

def cadastrar_pintor(artistas):
    while True:
        print("-"*25)
        print(f'{"Cadastro de usuários":^25}')
        print("-"*25)

        nome = input("Nome do Artista: ")
        data = input("daata de Nascimento:  ")
        local = input("Local de nascimento:  ")
        biografia = input("Biografia do Artista: ")
        estilo = input("Estilo do Artista: ")

        for artista in artistas:
            if nome == artista["nome"]:
                print('Usuario já existente.')
                continue

        artistas.append({"nome":nome, "data":data, "local":local, "biografia":biografia, "estilo":estilo})
        print('Usuário cadastrado!')
        break

# Gerenciar Obras
def gerenciar_obras(obras_cadastradas):
    while True:
        print("-"*27)
        print(f'{"Gerenciamento de Obras":^27}')
        print("-"*27)
        print("1 - Adicionar Obras ")
        print("2 - Remover Obras ")
        print("3 - Listar Obras ")
        print("4 - Voltar a Pagina Inicial")
        Escolha = input("\nEscolha uma das alternativas: ")
     
        if Escolha == "1": 
            print("-"*25)
            print("Tela de Adicionar Obras")
            print("-"*25)
            titulo = input("Digite o Titulo: ")
            print("-"*25)
            autor = input("Digite o Nome Autor: ")
            print("-"*25)
            data_de_lançamento = input("Digite a Data de Lançamento: ")
            print("-"*25)
            print("Obras Cadastrado!!")
            print("-"*25)
            obras_cadastradas.append(titulo)
        
        elif Escolha == "2": 
            Nome_do_Obras_remover = input("Digite o nome do Obras que vc quer Remover: ")
            if Nome_do_Obras_remover in obras_cadastradas:
                obras_cadastradas.remove(Nome_do_Obras_remover)
            
        
        elif Escolha == "3":
            print("-"*25)
            print(f'{"Lista de Obras:":^25}')
            print("-"*25)
            for Obras in obras_cadastradas:
                print('-',Obras)
        elif Escolha == "4": 
            break
        
        else: 
            print("escolha uma opção válida")

def criar_log(users, nome):
    with open('log', 'w') as log:
        log.write(f"O usuario {nome} foi adicionado ao sistema!")