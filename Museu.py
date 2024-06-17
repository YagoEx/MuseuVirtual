import functionss

users = [
    {"login": "admin", "password": "admin", "acess": "administrator"},
    {"login": "Gabriel", "password": "2004", "acess": "comum"},
    {"login": "albert123", "password": "1968", "acess": "comum"},
]

with open("Caravaggio.txt", "r", encoding="utf-8") as arquivo:
    caravaggio = arquivo.read()
with open("Michelangelo.txt","r", encoding="utf-8") as arquivo:
    michelangelo = arquivo.read()



artistas = [
    {"nome": "Michelangelo", "data": "06/03/1475", "local": "Italia", "biografia": michelangelo, "estilo": "Renascentismo", "obras": ["O beijo", "Abaporu"]},
    {"nome": "Caravaggio", "data": "29/09/1571", "local": "Italia", "biografia": caravaggio, "estilo": "Barroco", "obras": ["A noite Estrelada", "Mona lisa"]}
]

incursoes = [
    {"school": "Oscar de Macedo", "quantity": "30", "theme": "renascentismo", "guide": "neo-renascentismo", "date": "10/08"}
]

incursao = []

obras_cadastradas = ["Mona Lisa", "A noite Estrelada", "O Beijo", "Abaporu"]

obras_reservadas = []

def main():
    validation = functionss.login(users) 
    while True:
        if validation == "administrator":
            while True: 
                print('')
                print("-"*25)
                print(f'{"Museu Virtual:":^25} ')    
                print("1 - Pesquisar Obras")
                print("2 - Obras Reservadas")
                print("3 - Cancelar Reservas")
                print("4 - Incursões")
                print("5 - Gerenciar Usuarios")
                print("6 - Sair")

                selecao = input("Selecione uma das opções à cima: ")
                try: 
                    int(selecao)
                    if int(selecao) > 6: 
                        print("Digite somente as opções validas.")
                        continue
                except ValueError:
                    print('digite somente as opções validas.')
                    continue
                if selecao == "1":
                    print("-"*25)
                    print(f"{"Pesquisar Obras":^25}")
                    print("-"*25)

                    obras = []
                    
                    for artista in artistas:
                        for obra in artista["obras"]:
                            obras.append(obra) 

                    obras_sort = functionss.quick_sort(obras)
                    artistas_list = []
                    
                    for artista in artistas:
                        artistas_list.append(artista["nome"])
                    while True:
                        pesquisa = int(input("1- Pesquisar por título \n2- Pesquisar por Artista \nResposta:  "))
                        print(obras_sort)
                        if pesquisa == 1:
                            busca = input("Digite o título da obra: ").capitalize()
                            print(busca)
                            disponibilidade = functionss.busca_binaria(obras_sort, busca)

                            if disponibilidade == -1: 
                                print("Obra não encontrada!")
                                continue

                            else:
                                reservar = input("A Obra foi encontrada. Deseja reserva-la? [S/N] ").lower()
                                if reservar == "s": 
                                    obras_reservadas.append(busca)
                                    print("\nObra Reservada!")
                                    break

                        elif pesquisa == 2:
                            artistas_sort = functionss.quick_sort(artistas_list)
                            print(artistas_sort)

                            busca_artista = input("Qual artista você deseja buscar? ").capitalize()
                            artista_encontrado = None
                            
                            for artista in artistas:
                                if artista["nome"] == busca_artista:
                                    artista_encontrado = artista
                                    

                            if artista_encontrado:
                                for item, valor in artista_encontrado.items():
                                    print(f"{item}: {valor}")
                            else: 
                                print("Artista não encontrado!")
                        else:
                            print("escolha uma opção válida")

                elif selecao == "2":
                    print("-"*25)
                    print(f"{"Obras Reservadas:":^25}")
                    print("-"*25)
                    for Obras in obras_reservadas:
                        print("-",Obras)
                        print('''''')
                        
                elif selecao == "3":
                    Nome_do_Obras_remover = input("Digite o nome da Obra que vc quer Remover: ")
                    if Nome_do_Obras_remover in obras_reservadas:
                        obras_reservadas.remove(Nome_do_Obras_remover)
                        print("Reserva Cancelada!")
                



                elif selecao == "4":
                     print("-"*25)
                     print(f"{"Incursões:":^25}")
                     print("-"*25)
                     escola = input("Digite o nome da escola: ")
                     quantidade = input("Digite a quantidade de pessoas a realizar a incursão: ")
                     tema = input("Digite o tema que deseja ser incursado: ")
                     roteiro =  input("Digite o roteiro que se deseja percorrer: ")
                     data = input("Digite a data da incursão: ")
                     for incursoes in incursao:
                         incursoes.append({"school":escola, "quantity":quantidade, "theme":tema, "guide":roteiro, "date":data})
                     functionss.criar_log(incursao, escola)
                     print("Incursão marcada!!")

                elif selecao == "5":
                    functionss.gerenciar_usuarios(users)

                elif selecao == "6":
                    break    
        
        elif validation == "comum":
            while True:
                print("-"*25)
                print(f'{"Museu Virtual:":^25} ')
                print("-"*25)
                print("1 - Pesquisar Obras")
                print("2 - Obras Reservados")
                print("3 - Cancelar reserva")
                print("4 - Sair\n")

                selecao = input("Selecione uma das opções acima: ")
                
                if  selecao == "1":
                    print("-"*25)
                    print(f'{"Pesquisar Obras":^25}')
                    print("-"*25)

                    obras = []
                    
                    for artista in artistas:
                        for obra in artista["obras"]:
                            obras.append(obra) 

                    obras_sort = functionss.quick_sort(obras)
                    artistas_list = []
                    
                    for artista in artistas:
                        artistas_list.append(artista["nome"])
                    while True:
                        pesquisa = int(input("1- Pesquisar por título \n2- Pesquisar por Artista \nResposta:  "))
                        print(obras_sort)
                        if pesquisa == 1:
                            busca = input("Digite o título da obra: ").capitalize()
                            print(busca)
                            disponibilidade = functionss.busca_binaria(obras_sort, busca)

                            if disponibilidade == -1: 
                                print("Obra não encontrada!")
                                continue

                            else:
                                reservar = input("A Obra foi encontrada. Deseja reserva-la? [S/N] ").lower()
                                if reservar == "s": 
                                    obras_reservadas.append(busca)
                                    print("\nObra Reservada!")
                                    break
                    break
                        
                elif selecao == "2":
                    print("-"*25)
                    print(f'{"Obras Reservados:":^25}')
                    print("-"*25)
                    for Obras in obras_reservadas:
                        print('-',Obras)
                    print('''''')
                elif selecao == "3":
                    cancelar_reserva = input("Digite o nome da Obra que deseja cancelar a reserva: ")
                    if cancelar_reserva in obras_reservadas:
                        obras_reservadas.remove(cancelar_reserva)
                
                elif selecao == "4":
                     print("-"*25)
                     print(f"{"Incursões:":^25}")
                     print("-"*25)
                     escola = input("Digite o nome da escola: ")
                     quantidade = input("Digite a quantidade de pessoas a realizar a incursão: ")
                     tema = input("Digite o tema que deseja ser incursado: ")
                     roteiro =  input("Digite o roteiro que se deseja percorrer: ")
                     data = input("Digite a data da incursão: ")
                     for incursoes in incursao:
                         incursoes.append({"school":escola, "quantity":quantidade, "theme":tema, "guide":roteiro, "date":data})
                     functionss.criar_log(incursao, escola)
                     print("Incursão marcada!!")

                elif selecao == "5":
                    break            

            break
        break 

              



if __name__ == "__main__":
    main()
