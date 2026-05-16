def ler_novo_texto():
    """
    Solicita ao usuário o texto de uma notícia.

    A função valida a entrada e não permite textos vazios
    ou compostos apenas por espaços em branco.

    Retorno:
        str:
            Texto válido digitado pelo usuário.
    """
    while True:
        texto = input("Digite o texto: ")

        # Validação do texto digitado
        if texto.strip() != "":
            return texto
        else:
            print("Texto não pode ser vazio. Tente novamente.")