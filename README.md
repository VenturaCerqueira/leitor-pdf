# 🧑‍💻 Extrator de Servidores Públicos - Prefeitura de Riachão do Jacuípe

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Este projeto oferece uma solução simples e eficaz para extrair nomes e CPFs de servidores públicos a partir de um arquivo PDF. O resultado é uma planilha Excel limpa, contendo apenas os dados essenciais, e um log detalhado das linhas que não puderam ser processadas.

---

## 🎯 Objetivo

O principal objetivo deste script é automatizar a coleta de informações cruciais (Nome e CPF) de servidores listados em um PDF, facilitando a análise e o uso desses dados em outras aplicações ou sistemas.

## ✨ Como Funciona

1.  **Leitura do PDF**: O script inicia lendo o conteúdo textual de cada página do arquivo PDF especificado.
2.  **Extração Focada**: Para cada linha lida, o script tenta identificar e extrair o CPF e o Nome do servidor. A lógica é robusta para lidar com variações na formatação do PDF.
3.  **Saída Organizada**: Os dados extraídos com sucesso são compilados em uma planilha Excel fácil de usar.
4.  **Registro de Linhas Ignoradas**: Linhas que não se encaixam no padrão esperado para um registro de servidor (principalmente pela ausência ou inconsistência do CPF) são cuidadosamente registradas em um arquivo de log para revisão e depuração.

## ⚙️ Requisitos

Para executar este script, você precisará ter o Python instalado e as seguintes bibliotecas:

* **Python**: Versão 3.8 ou superior.
* [`pdfplumber`](https://pypi.org/project/pdfplumber/): Para extrair texto de PDFs.
* [`pandas`](https://pypi.org/project/pandas/): Para manipulação e exportação de dados em Excel.

## 🚀 Instalação

Abra seu terminal ou prompt de comando e execute o seguinte comando para instalar as dependências:

```bash
pip install pdfplumber pandas
```
