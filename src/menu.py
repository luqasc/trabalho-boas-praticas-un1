from src.noticias import adicionar_noticia, listar_noticias
from src.classificacao import classificacao_manual, classificacao_automatica
from src.utils import ler_novo_texto

def menu_principal():
    """
    Exibe e controla o menu principal da aplicação, chamando 
    as funções adequadas.

    O menu permite ao usuário:
        - adicionar notícias manualmente;
        - adicionar notícias com classificação automática;
        - listar notícias cadastradas;
        - encerrar o programa.

    A função permanece em execução até que o usuário escolha
    a opção de saída.
    """

    while True:
        print("1 - Adicionar notícia com classificação manual")
        print("2 - Adicionar notícia com classificação automática")
        print("3 - Listar notícias")
        print("4 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            texto = ler_novo_texto()
            classificacao = classificacao_manual()

            adicionar_noticia(texto, classificacao)

        elif opcao == "2":
            texto = ler_novo_texto()
            classificacao = classificacao_automatica(texto)

            adicionar_noticia(texto, classificacao)

        elif opcao == "3":
            listar_noticias()

        elif opcao == "4":
            print("Encerrando sistema.")
            break

        else:
            print("Digite uma opção válida (1, 2, 3 ou 4).")