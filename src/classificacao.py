from src.constantes import CLASSIFICACOES_VALIDAS

def classificacao_manual():
    """
    Solicita ao usuário uma classificação manual para uma notícia.

    A função continua solicitando entrada até que uma classificação
    válida seja digitada.

    Classificações aceitas:
        - "confiável"
        - "duvidosa"
        - "falsa"

    Retorno:
        str:
            Classificação válida digitada pelo usuário.
    """

    while True:
        classificacao = input("Digite a classificação (\"confiável\", \"duvidosa\", \"falsa\"): ")

        # Padronização da classificação digitada
        classificacao = classificacao.strip().lower()

        # Validação da classificação digitada
        if classificacao in CLASSIFICACOES_VALIDAS:
            return classificacao
        
        print("Classificação inválida. Tente novamente.")

def classificacao_automatica(texto):
    """
    Classifica automaticamente uma notícia com base em critérios
    simples de suspeição.

    Os critérios analisados incluem:
        - Presença de palavras-chave suspeitas;
        - Ausência de fonte explícita;
        - Extensão do texto (textos muito curtos podem ser considerados menos confiáveis).

    Cada critério aumenta a pontuação de suspeição da notícia.

    Parâmetros:
        texto (str):
            Texto da notícia a ser analisado.

    Retorno:
        str:
            Classificação atribuída automaticamente:
            - "confiável"
            - "duvidosa"
            - "falsa"
    """
    # Pontuação de suspeição da notícia
    suspicion_score = 0

    # Padronização do texto para facilitar a checagem de critérios
    texto_normalizado = texto.upper()

    # Checagem de critérios
    if "FONTE" not in texto_normalizado:
        suspicion_score = suspicion_score + 1
    if "!!!" in texto_normalizado:
        suspicion_score = suspicion_score + 1
    if "URGENTE" in texto_normalizado:
        suspicion_score = suspicion_score + 1
    if len(texto) < 10:
        suspicion_score = suspicion_score + 1

    # Classificação final com base na pontuação de suspeição
    if suspicion_score == 0:
        return "confiável"
    elif suspicion_score == 1:
        return "duvidosa"
    else:
        return "falsa"