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

## Primeira analise de tópicos

Todos os comentários:
```
Tópicos para o arquivo processed/andrew_processed_prediction.csv:
Tópico 1:
    thank huberman thanks andrew dr information best amazing david us
Tópico 2:
    adhd focus im long help attention brain diagnosed find someone
Tópico 3:
    im right dopamine cold god minutes listening book watching please
Tópico 4:
    alcohol dopamine brain body dog use effects bit hair increase
Tópico 5:
    im drink drinking ive alcohol days feel fasting eating week
```

```
Tópicos para o arquivo processed/impaulsive_processed_prediction.csv:
Tópico 1:
    logan mark talking prime please wow awesome funny porn pod
Tópico 2:
    best ive eyes im logan watched first jeffrey jeffree interview
Tópico 3:
    logan im jeffree paul definitely saying always star sure ksi
Tópico 4:
    beast george mr cena john mrbeast jimmy weird haaland videos
Tópico 5:
    mike lana logan happens fucking cry fuck im annoying shit
```

```
Tópicos para o arquivo processed/lex_processed_prediction.csv:
Tópico 1:
    lex im interview thank voice jeff ive human bezos conversation
Tópico 2:
    money school kids education problem ben government schools children family
Tópico 3:
    lex israel hamas palestinians jews state gaza palestine bassem god
Tópico 4:
    destiny ben trump debate shapiro biden right left two im
Tópico 5:
    us war ukraine russia putin nato nuclear world power russian
```

Comentários com hate:
```
Tópicos para o arquivo processed/andrew_hate_comments.csv:
Tópico 1:
    fat alcohol david point us another science eating level stop
Tópico 2:
    thank ass well andrew nerd times enough im working looking
Tópico 3:
    shit im understand us piece adhd fat lazy money lets
Tópico 4:
    thank dopamine end self mean anything mind happy less stay
Tópico 5:
    huberman im bullshit dr right best whole new feel world
```

```
Tópicos para o arquivo processed/impaulsive_hate_comments.csv:
Tópico 1:
    bitch cuss beast mrbeast im mr dudes mikes whore funny
Tópico 2:
    mike shit fucking dumb lana ass literally girl money joke
Tópico 3:
    im mike shit george bitch fuck gay logan sure aint
Tópico 4:
    logan girl mike mark show hoe asshole probably pornstar jeffree
Tópico 5:
    logan jacksepticeye still paul next tho boy rich dumbass gets
```

```
Tópicos para o arquivo processed/lex_hate_comments.csv:
Tópico 1:
    destiny ben leftist jew shapiro im cuck another liberal brain
Tópico 2:
    israel us ukraine putin russia jews state country nukes war
Tópico 3:
    trump zionist war jews two biden ben destiny talking zionists
Tópico 4:
    lex israel jews hamas world palestinians bezos human rich arabs
Tópico 5:
    destiny ben debate shapiro moron right two liberal trump shit
```