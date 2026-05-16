# Sistema de Monitoramento de Fake News e Qualidade da Informação

## Descrição

Este projeto consiste em um sistema simples de armazenamento e classificação de notícias quanto à confiabilidade de seus conteúdos.

O programa permite ao usuário:

- adicionar notícias manualmente;
- classificar notícias manualmente;
- classificar notícias automaticamente;
- listar todas as notícias armazenadas.

A classificação automática utiliza critérios simples de suspeição baseados em:
- presença de palavras-chave suspeitas;
- ausência de fonte explícita;
- tamanho do texto.

---

# Estrutura do Projeto

```text
trabalho-boas-praticas-un1/
│
├── main.py
│
├── src/
│   ├── __init__.py
│   ├── constantes.py
│   ├── noticias.py
│   ├── classificacao.py
│   ├── utils.py
│   └── menu.py
│
└── README.md
```

---

# Funcionalidades

## Adição manual de notícias

O usuário pode inserir:
- o texto da notícia;
- a classificação manual:
  - confiável;
  - duvidosa;
  - falsa.

---

## Classificação automática

O sistema avalia automaticamente a notícia utilizando critérios simples de suspeição.

### Critérios analisados

- ausência da palavra `"FONTE"`;
- presença de `"!!!"`;
- presença da palavra `"URGENTE"`;
- textos muito curtos.

### Regras de classificação

| Pontuação de suspeição | Classificação |
|---|---|
| 0 | confiável |
| 1 | duvidosa |
| 2 ou mais | falsa |

---

## Listagem de notícias

O sistema permite visualizar:
- o texto de cada notícia;
- sua classificação correspondente.

---

# Tecnologias Utilizadas

- Python 3

---

# Como Executar

## 1. Clone o repositório

```bash
git clone https://github.com/luqasc/trabalho-boas-praticas-un1.git
```

---

## 2. Acesse a pasta do projeto

```bash
cd projeto_fake_news
```

---

## 3. Execute o programa

```bash
python main.py
```

---

# Exemplo de Uso

```text
1 - Adicionar notícia com classificação manual
2 - Adicionar notícia com classificação automática
3 - Listar notícias
4 - Sair

Opção: 2

Digite o texto:
URGENTE!!! Vacina causa mutação alienígena

Classificação atribuída:
falsa
```

---

# Autor

Lucas Cunha de Azevedo
Projeto desenvolvido para fins acadêmicos.