# Trabalho de Introdução à Ciência de Dados

**Integrantes:** [Caio Paiva](https://github.com/caiopaiva92), [João Arnaud](https://github.com/JoaoArnaud), [Eduardo Antônio](https://github.com/EduardoLeitaoFilho) e [Thiago Lacerda](https://github.com/Thiago-S-Lacerda)  
**Tema:** O impacto do contexto histórico e da indústria de jogos na escolha de hardware dos usuários.

## Visão geral

Este repositório reúne dados da pesquisa **Steam Hardware & Software Survey**, usada pela Steam para divulgar a distribuição de hardware e software entre seus usuários. O objetivo do trabalho é analisar como características como sistema operacional, memória RAM, CPU, placa de vídeo, VRAM e resolução principal de tela mudam ao longo do tempo, relacionando essas mudanças com o contexto histórico e com a evolução da indústria de jogos.

## Processo de coleta

A coleta foi feita por web scraping em snapshots históricos da página da pesquisa da Steam disponíveis no **Wayback Machine**. Os notebooks de extração definem listas de links mensais para cada ano, fazem requisições HTTP com `requests` e analisam o HTML com `BeautifulSoup`.

Em cada snapshot, o script procura as seções de interesse da pesquisa, como `OS Version`, `System RAM`, `Physical CPUs`, `Video Card Description`, `VRAM` e `Primary Display Resolution`. Para cada categoria, são extraídos o nome da especificação, o percentual de usuários e a variação mensal indicada pela Steam. Depois disso, o mês e o ano são adicionados manualmente ao registro antes da gravação em CSV.

As bases anuais foram geradas com `pandas` a partir das bases mensais. O procedimento usa o valor de dezembro como referência final do ano e calcula a variação anual subtraindo o percentual da primeira aparição daquela especificação no mesmo ano. Essa escolha evita distorções quando uma peça, sistema ou configuração aparece ao longo do ano, mas não existe na base de janeiro.

## Categorias analisadas

As principais categorias coletadas são:

| Categoria | Descrição |
| --- | --- |
| `OS Version` | Sistemas operacionais e versões usados pelos usuários. |
| `System RAM` | Quantidade de memória RAM instalada. |
| `Physical CPUs` | Quantidade de CPUs físicas ou núcleos reportados pela pesquisa. |
| `Video Card Description` | Modelos de placas de vídeo. |
| `VRAM` | Quantidade de memória de vídeo. |
| `Primary Display Resolution` | Resolução principal de tela. |

Alguns arquivos podem conter categorias adicionais ou variações conforme o ano e a disponibilidade dos dados na página arquivada.

## Dicionário de dados

### Arquivos mensais

Arquivos no formato `dados_mensais_<ano>.csv`.

| Nome da coluna | Descrição | Exemplo |
| --- | --- | --- |
| `Categoria` | Grupo da pesquisa de hardware/software ao qual a linha pertence. | `OS Version` |
| `Especificação` | Item específico dentro da categoria. | `Windows 11 64 bit` |
| `Porcentagens` | Percentual de usuários da Steam que possuem aquela especificação no mês. | `53.46%` |
| `Incrementos/Decrementos` | Variação mensal informada pela Steam para a especificação. | `+0.34%` |
| `Mês` | Mês ao qual o snapshot foi associado na coleta. | `Janeiro` |
| `Ano` | Ano de referência do registro. | `2025` |

### Arquivos anuais

Arquivos no formato `dados_anuais_<ano>.csv`.

| Nome da coluna | Descrição | Exemplo |
| --- | --- | --- |
| `Categoria` | Grupo da pesquisa de hardware/software ao qual a linha pertence. | `OS Version` |
| `Especificação` | Item específico dentro da categoria. | `Windows` |
| `Porcentagens` | Percentual final usado como referência anual, normalmente o valor de dezembro. | `96.4` |
| `Incrementos/Decrementos` | Diferença entre o percentual final do ano e o percentual da primeira aparição da especificação naquele ano. | `0.38` |
| `Ano` | Ano de referência do registro. | `2023` |

