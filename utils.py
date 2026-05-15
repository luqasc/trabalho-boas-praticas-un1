def ler_novo_texto():
    """
    Recebe e valida novos textos inseridos pelo usuário.
    Não aceita textos vazios.
    """
    while(True):
        texto = input("Digite o texto: ")

        # Validação do texto digitado (não pode ser vazio)
        if texto.strip() != "":
            return texto
        else:
            print("Texto não pode ser vazio. Tente novamente.")