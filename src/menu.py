from src.noticias import adicionar_noticia, listar_noticias
from src.classificacao import classificacao_manual, classificacao_automatica
from src.utils import ler_novo_texto

def menu_principal():
    """
    Menu principal da aplicação.
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
            break
        else:
            print("Digite uma opção válida (1, 2, 3 ou 4).")