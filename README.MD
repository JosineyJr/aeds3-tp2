# Trabalho Prático 2

## Visão Geral
Este projeto é uma aplicação web que utiliza a codificação de Huffman para compressão e descompressão de arquivos de texto. Construída com o microframework Flask em Python, a aplicação fornece uma interface simples e intuitiva para o upload de arquivos e download dos arquivos processados.

## Funcionalidades
- Compressão de arquivos de texto usando o algoritmo de Huffman.
- Download de arquivos comprimidos com a extensão `.huf`.
- Descompressão de arquivos `.huf` e recuperação do texto original.
- Interface amigável que permite visualizar o conteúdo do arquivo antes da compressão e descompressão.

## Pré-requisitos
- Python 3.9+
- Flask

## Configuração do Ambiente
Para executar a aplicação, você precisará configurar o ambiente seguindo os passos abaixo:

### Instalação do Python
Certifique-se de ter o Python 3.6 ou superior instalado em seu sistema. Caso não tenha, faça o download no site oficial do Python: [Python Download](https://www.python.org/downloads/).

### Dependências
Para instalar as dependências do projeto, execute:
```bash
make install
```

Ou:

```bash
pip install -r requirements.txt
```

## Execução da Aplicação
Com o ambiente pronto, inicie o servidor Flask com o comando:
```bash
make run
```
Ou:
```bash
flask run
```

A aplicação estará acessível em `http://localhost:5000/`.