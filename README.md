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
    - `models`: modelos do algoritmo.
    - `processing`: pré-processamento dos dados.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](https://github.com/brunofaria27/youtube-hatespeech/blob/main/LICENSE) para mais detalhes.