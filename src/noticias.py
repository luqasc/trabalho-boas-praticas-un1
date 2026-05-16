from src.constantes import CLASSIFICACOES_VALIDAS

# Lista global de notícias, onde cada notícia é representada como um dicionário
# Cada dicionário contém o texto e sua classificação
noticias = []

def adicionar_noticia(texto, classificacao = None):
    """
    Adiciona uma nova notícia à lista global de notícias.

    A função valida o formato do texto e da classificação antes 
    de armazenar a notícia no sistema.

    Parâmetros:
        texto (str):
            Texto da notícia.

        classificacao (str):
            Classificação atribuída à notícia.
            Deve ser "confiável", "duvidosa" ou "falsa".

    Exceções:
        TypeError:
            Lançada caso o texto não seja do tipo string.

        ValueError:
            Lançada caso o texto esteja vazio ou a classificação
            seja inválida.
    """

    # Validações de formato do texto e da classificação
    if not isinstance(texto, str):
        raise TypeError("Texto deve ser string.")

    if texto.strip() == "":
        raise ValueError("Texto vazio.")

    if classificacao not in CLASSIFICACOES_VALIDAS:
        raise ValueError("Classificação inválida.")
    
    # Criação e preenchimento do dicionário
    # As validações de formato do texto e da classificação são realizadas previamente, nas funções ler_novo_texto e classificacao_manual.
    noticia = {
        "texto": texto,
        "classe": classificacao
    }

    # Adição do dicionário à lista global de notícias
    noticias.append(noticia)

def listar_noticias():
    """
    Lista todas as notícias armazenadas no sistema.

    Para cada notícia cadastrada, exibe:
        - o texto da notícia;
        - sua classificação.

    Caso não existam notícias cadastradas, informa isso ao usuário.
    """
    # Checagem da existência de notícias cadastradas
    if not noticias:
        print("Nenhuma notícia cadastrada.")
        return

    # Listagem
    for noticia in noticias:
        print("Texto:", noticia["texto"])
        print("Classificação:", noticia["classe"])
        print("-------------------")