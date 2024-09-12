# Detecção de Discurso de Ódio em Podcasts do YouTube

## Descrição
Este projeto tem como objetivo detectar discurso de ódio em podcasts do YouTube utilizando abordagens de inteligência artificial. O trabalho é parte do meu TCC para a graduação em Ciência da Computação.

## Tabela de Conteúdos
- [Instalação](#instalação)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Licença](#licença)

## Instalação
1. Clone o repositório:
    ```bash
    $ git clone https://github.com/brunofaria27/youtube-hatespeech.git
    ```
2. Entre no diretório do projeto:
    ```bash
    $ cd youtube-hatespeech
    ```

## Estrutura do projeto
- `youtube-extract`: projeto Java que extrai comentários do YouTube e armazena no MongoDB.
- `analytics`: scripts em Python utilizando IA para ver a quantidade de discurso de ódio.
    - `processing`: pré-processamento dos dados.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](https://github.com/brunofaria27/youtube-hatespeech/blob/main/LICENSE) para mais detalhes.

## Rodar código
```bash
python -m venv myenv
myenv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

https://maartengr.github.io/BERTopic/index.html#installation

- Rodar BERTopic e WordCloud (saida BERTopic) para todos comentarios + reply de cada podcast - OK
- Rodar BERTopic e WordCloud (saida BERTopic) para todos comentarios de hate + reply de cada podcast - OK
- Proporção de quantos replies para cada comnetario - TODOS
- Proporção de quantos replies para cada comnetario - HATE
- Proporcao de quantidade de hates em todos os comentarios de reply

- O hate é para a pessoa/convidado ou para a ideia da pessoa/convidado?

Levando em consideracao os comentarios nao vem na ordem fica complicado de achar o momento do video o que vamos fazer é se o hate esta relacionado aos topicos principais do video