def classificacao_manual():
    """
    Recebe e valida a classificação de um texto pelo usuário.
    Exige que a classificação digitada pertença a uma das três categorias
    """
    while True:
        classificacao = input("Digite a classificação (\"confiável\", \"duvidosa\", \"falsa\"): ")

        # Padronização da classificação digitada
        classificacao = classificacao.strip().lower()

        # Validação da classificação digitada
        if classificacao in ["confiável", "duvidosa", "falsa"]:
            return classificacao
        else:
            print("Classificação inválida. Tente novamente.")

def classificacao_automatica(texto):
    """
    Avalia o texto de uma notícia e classifica-a automaticamente como "confiável", "duvidosa" ou "falsa" com base em critérios simples:
    - Presença de palavras-chave suspeitas;
    - Ausência de fonte explícita;
    - Extensão do texto (textos muito curtos podem ser considerados menos confiáveis).
    """
    # Pontuação de suspeição da notícia
    suspicion_score = 0

    # Checagem de critérios
    if "FONTE" not in texto:
        suspicion_score = suspicion_score + 1
    if "!!!" in texto:
        suspicion_score = suspicion_score + 1
    if "URGENTE" in texto:
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