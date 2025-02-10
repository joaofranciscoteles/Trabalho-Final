# Análise de Coocorrência de Produtos com Grafos e Sistema de Recomendação
<div style="display: inline-block;">
<img align="center" height="20px" width="60px" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> 
<img align="center" height="20px" width="80px" src="https://img.shields.io/badge/Made%20for-VSCode-1f425f.svg"/> 
</a> 
</div>

## Introdução

Este repositório contém um conjunto de scripts Python que processam dados da base de dados Instacart, criam grafos de coocorrência entre produtos e geram um sistema de recomendação baseado nesses grafos. O objetivo é recomendar produtos aos usuários com base nas coocorrências de compras dentro de diferentes departamentos de uma loja.

A base de dados original pode ser baixada no **[Kaggle - Instacart Market Basket Analysis](https://www.kaggle.com/c/instacart-market-basket-analysis/data)**. Os arquivos necessários são:

- `order_products__prior.csv`: Contém informações sobre os pedidos e os produtos comprados.
- `products.csv`: Informações sobre os produtos, como nome e ID.
- `departments.csv`: Informações sobre os departamentos aos quais os produtos pertencem.

Estes arquivos devem ser baixados e colocados na pasta `base_de_dados`. Além disso, a base de dados processada já está disponível no **Zenodo** pelo seguinte link: [Acesso à Base Processada](X).

---

## Fluxo de Processamento

O sistema é dividido em várias etapas, onde um script depende do anterior para gerar o próximo resultado.

### 📌 Códigos Principais

1. **Processamento de Dados (`processamento.py`)**
   - **Entrada**: Arquivos CSV da base de dados (`order_products__prior.csv`, `products.csv`, `departments.csv`).
   - **Descrição**: Processa e integra os dados dos pedidos, produtos e departamentos, gerando um único arquivo consolidado.
   - **Saída**: `processed_data_with_departments.csv` (salvo na pasta `base_de_dados`).

2. **Geração de Grafos de Coocorrência (`graph_generator.py`)**
   - **Entrada**: `processed_data_with_departments.csv`.
   - **Descrição**: Cria 21 grafos de coocorrência entre produtos, um para cada departamento.
   - **Saída**: Arquivos `.gpickle` na pasta `base_de_dados`.

3. **Visualização de Grafos (`graph_visualization.py`)**
   - **Entrada**: Um dos arquivos `.gpickle` gerados pelo `graph_generator.py`.
   - **Descrição**: Gera uma visualização do grafo desejado.
   - **Saída**: Visualização gráfica interativa ou estática.

4. **Geração de Árvore Máxima de Coocorrência (`arvore_maxima.py`)**
   - **Entrada**: Arquivos `.gpickle` gerados pelo `graph_generator.py`.
   - **Descrição**: Aplica o algoritmo de Árvore Geradora Mínima (MST) e salva os novos grafos com MST aplicada.
   - **Saída**: Arquivos `.gpickle` na pasta `Grafos_MST_maxima`.

5. **Sistema de Recomendação (`sistema_recomendacao.py`)**
   - **Entrada**: Grafos `.gpickle` processados pelo `arvore_maxima.py`.
   - **Descrição**: Permite ao usuário inserir um produto e receber recomendações baseadas nas coocorrências.
   - **Saída**: Recomendações exibidas no terminal.

6. **Cálculo da Densidade dos Grafos (`density_calculator.py`)**
   - **Entrada**: Arquivos `.gpickle` gerados pelo `graph_generator.py`.
   - **Descrição**: Calcula a densidade de cada grafo de departamento e salva os resultados.
   - **Saída**: Arquivo `densidade_grafos.csv` salvo na pasta `dados`.

---

### 📌 Códigos Geradores de Dados para o Artigo

7. **Comparação entre Grafos Originais e MST (`comparacao_mst.py`)**
   - **Entrada**: Arquivos `.gpickle` dos grafos originais e das MSTs.
   - **Descrição**: Compara estatísticas (número de nós, arestas e pesos médios) entre os grafos originais e as árvores geradas.
   - **Saída**: `comparacao_mst.csv` salvo na pasta `dados` + gráficos comparativos.

8. **Identificação das Conexões Mais Fortes (`conexoes_fortes.py`)**
   - **Entrada**: Arquivo `.gpickle` de um grafo MST gerado pelo `arvore_maxima.py`.
   - **Descrição**: Extrai as 10 conexões mais fortes (arestas de maior peso) do grafo.
   - **Saída**: `top_10_conexoes.csv` salvo na pasta `dados`.

9. **Visualização das Conexões Mais Fortes (`conexoes_fortes_visualization.py`)**
   - **Entrada**: Arquivo gerado pelo `conexoes_fortes.py`.
   - **Descrição**: Cria uma visualização gráfica interativa e uma imagem estática das 10 conexões mais fortes.
   - **Saída**: `grafo_top_10.html` (visualização interativa) e `grafo_top_10.png` (imagem).

10. **Top 10 Mais e Menos Vendidos por Departamento (`top10_mais_menos_vendidos.py`)**
   - **Entrada**: `processed_data_with_departments.csv`.
   - **Descrição**: Calcula os 10 produtos mais vendidos e os 10 menos vendidos nos departamentos "Produce" e "Personal Care".
   - **Saída**: `relatorio_vendas_departamentos.csv` salvo na pasta `dados` + gráficos.

11. **Total de Vendas por Departamento (`total_vendas_por_departamento.py`)**
   - **Entrada**: `processed_data_with_departments.csv`.
   - **Descrição**: Calcula o total de vendas por departamento e gera uma visualização gráfica.
   - **Saída**: `vendas_por_departamento.csv` e `vendas_por_departamento.png` salvos na pasta `dados`.

12. **Vendas por Produto (`vendas_por_produto.py`)**
   - **Entrada**: `processed_data_with_departments.csv`.
   - **Descrição**: Calcula o total de vendas por produto nos departamentos "Produce" e "Personal Care".
   - **Saída**: Arquivos CSV separados por departamento na pasta `dados`.

---

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





