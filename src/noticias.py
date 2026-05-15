# Lista global de notícias, onde cada notícia é representada como um dicionário
# Cada dicionário contém o texto e sua classificação
noticias = []

def adicionar_noticia(texto, classificacao = None):
    """
    Adiciona uma notícia à lista global de notícias.
    Para isso, armazena seu texto e sua classificação em um dicionário, adicionando-o posteriormente à lista.
    """

    # Validações de formato do texto e da classificação
    if not isinstance(texto, str):
        raise TypeError("Texto deve ser string.")

    if texto.strip() == "":
        raise ValueError("Texto vazio.")

    if classificacao not in ["confiável", "duvidosa", "falsa"]:
        raise ValueError("Classificação inválida.")
    
    # Criação e preenchimento do dicionário
    # As validações de formato do texto e da classificação são realizadas previamente, nas funções ler_novo_texto e classificacao_manual.
    dicionario = {}
    dicionario["texto"] = texto
    dicionario["classe"] = classificacao

    # Adição do dicionário à lista global de notícias
    noticias.append(dicionario)

def listar_noticias():
    """
    Lista todas as notícias armazenadas, mostrando o texto e a classificação de cada uma.
    """
    # Checagem da existência de notícias cadastradas
    if len(noticias) == 0:
        print("Nenhuma notícia cadastrada.")
        return

    # Listagem
    for i in range(0, len(noticias)):
        print("Texto:", noticias[i]["texto"])
        print("Classificação:", noticias[i]["classe"])
        print("-------------------")