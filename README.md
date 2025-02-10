# Análise de Coocorrência de Produtos com Grafos e Sistema de Recomendação
<div style="display: inline-block;">
<img align="center" height="20px" width="60px" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> 
<img align="center" height="20px" width="80px" src="https://img.shields.io/badge/Made%20for-VSCode-1f425f.svg"/> 
</a> 
</div>

## Introdução

Este repositório contém um conjunto de scripts Python que processa dados de uma base de dados de produtos, cria grafos de coocorrência entre os produtos e gera um sistema de recomendação baseado em grafos. O objetivo é recomendar produtos aos usuários com base nas coocorrências de compras de outros produtos dentro de diferentes departamentos de uma loja.

A base de dados usada é composta pelos seguintes arquivos:

- `order_products__prior.csv`: Contém informações sobre os pedidos e os produtos comprados.
- `products.csv`: Informações sobre os produtos, como nome e ID.
- `departments.csv`: Informações sobre os departamentos aos quais os produtos pertencem.

Estes arquivos podem ser baixados diretamente no site Kaggle - Instacart Market Basket Analysis.

## Fluxo de Processamento

O sistema é dividido em várias etapas, onde um script depende do anterior para gerar o próximo resultado:

1. **Processamento de Dados (`processamento.py`)**:
   - O script carrega e processa os dados dos arquivos CSV, integrando as informações de pedidos, produtos e departamentos. O resultado é um arquivo CSV com os dados processados, necessário para os próximos passos.

2. **Geração de Grafos de Coocorrência (`graph_generator.py`)**:
   - O script lê o arquivo processado e cria grafos de coocorrência para cada departamento, onde os nós representam os produtos e as arestas representam a coocorrência de produtos em pedidos. Os grafos são salvos em arquivos `.gpickle`.

3. **Visualização de Grafos (`graph_vizualization.py`)**:
   - Neste script, é necessário colocar o arquivo `.gpickle` correspondente do grafo que se deseja visualizar. O script gera uma visualização interativa utilizando Plotly, ou uma versão estática com Matplotlib, dependendo do tamanho do grafo.

4. **Geração de Árvore Máxima de Coocorrência (`arvoremaxima.py`)**:
   - O script gera uma árvore de extensão máxima (MST) para cada grafo criado no código `graph_generator`, baseada no peso das arestas. Ele salva esses grafos como novos arquivos `.gpickle` em uma pasta específica.

5. **Cálculo da Densidade dos Grafos (`densitycalculator.py`)**:
   - Este script calcula e exibe a densidade de cada grafo de departamento, tanto em uma tabela como em um gráfico de barras.

6. **Sistema de Recomendação de Produtos (`sistemarecomendacao.py`)**:
   - Utilizando os grafos de MST gerados, o script permite que o usuário insira uma lista de produtos e receba recomendações de outros produtos relacionados, baseadas nas coocorrências.

7. **Cálculo do Grau dos Produtos (`calculograu.py`)**:
   - Este script calcula o grau de cada nó em dois grafos de departamentos específicos, determinando os produtos mais conectados (com maior grau).

8. **Conexões Fortes (`conexoes_fortes.py`)**:
   - O script `conexoes_fortes.py` tem como objetivo carregar um grafo no formato `.gpickle` (o caminho do grafo pode ser alterado através da variável `input_file` no código), verificar se o grafo contém pesos nas arestas e extrair as 10 conexões mais fortes, ou seja, as arestas com maior peso. Estas conexões são então salvas em um arquivo CSV, que pode ser utilizado para análises posteriores ou para visualização dos produtos mais fortemente conectados.

9. **Visualização das Conexões Fortes (`conexoes_fortes_visualization.py`)**:
   - O script `conexoes_fortes_visualization.py` tem como objetivo criar e visualizar um grafo com as 10 conexões mais fortes entre produtos, com base em um conjunto de dados predefinido de conexões gerado pelo código `conexoes_fortes.py`. O grafo gerado pode ser visualizado de duas formas: uma visualização interativa utilizando Plotly e uma versão estática utilizando Matplotlib.

10. **Top 10 Mais Vendidos e Menos Vendidos de Cada Departamento (Produce e Personal Care) (`top10_mais_menos_vendidos.py`)**:
   - O script `top10_mais_menos_vendidos.py` tem como objetivo analisar os dados de vendas de produtos, identificando os 10 produtos mais vendidos e os 10 menos vendidos em departamentos específicos. Ele processa os dados de vendas em chunks, calcula a quantidade vendida de cada produto e gera gráficos para os 10 produtos mais vendidos e os 10 menos vendidos de cada departamento. O relatório final é salvo em um arquivo CSV.

11. **Total de Vendas para Cada Departamento (`total_vendas_por_departamento.py`)**:
   - O script `total_vendas_por_departamento.py` tem como objetivo analisar a quantidade total de vendas por departamento, gerando uma tabela com o total de vendas de cada departamento, bem como um gráfico de barras horizontal. O relatório final é salvo em um arquivo CSV e o gráfico gerado é salvo em formato PNG.

12. **Vendas por Produto (`vendas_por_produto.py`)**:
   - O script `vendas_por_produto.py` tem como objetivo calcular o total de vendas por produto para departamentos específicos. O script processa os dados de vendas, agrupa as informações por departamento e produto, e salva o total de vendas por produto em um arquivo CSV para cada departamento.

13. **Acesso ao Projeto**:
   - O acesso ao trabalho completo pode ser obtido através desse link do Google Drive: [Acesso ao projeto](https://drive.google.com/drive/folders/1AJ6vPFUd2RKiaVoqWz9Znyx31C4fYq-6?usp=sharing)



## Tecnologias Utilizadas

O projeto foi desenvolvido em Python, utilizando as seguintes bibliotecas:

```python
import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pickle
import tkinter as tk
from tkinter import ttk, messagebox
import collections
import difflib

```
## Instalação das Dependências

Para rodar o código, é necessário instalar as bibliotecas utilizadas. Use o comando `pip install` para instalar as dependências.


pip install pandas networkx matplotlib plotly tkinter





