import pickle
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import os

def carregar_grafo(caminho_arquivo):
    with open(caminho_arquivo, 'rb') as f:
        return pickle.load(f)

grafo_produce = carregar_grafo('grafo_departamento_4.gpickle')  
grafo_personal_care = carregar_grafo('grafo_departamento_11.gpickle')  

print("Grafos carregados com sucesso!")


if not os.path.exists('dados'):
    os.makedirs('dados')

def calcular_top_10_grau(grafo, nome_departamento):
    
    degree_dict = dict(grafo.degree())
    
    degree_df = pd.DataFrame(degree_dict.items(), columns=['Produto', 'Grau'])
    
    top_10_degree = degree_df.nlargest(10, 'Grau')

    
    filename = os.path.join('dados', f'top_10_grau_{nome_departamento.lower().replace(" ", "_")}.csv')
    top_10_degree.to_csv(filename, index=False)
    
    plt.figure(figsize=(12, 6))
    plt.bar(top_10_degree['Produto'], top_10_degree['Grau'])
    plt.title(f"Top 10 Produtos com Maior Grau - {nome_departamento}")
    plt.xlabel("Produto")
    plt.ylabel("Grau (Número de Conexões)")
    plt.xticks(rotation=45, ha='right', wrap=True)
    plt.tight_layout()
    plt.show()

    print(f"Arquivo '{filename}' salvo com sucesso!")

calcular_top_10_grau(grafo_produce, "Produce")
calcular_top_10_grau(grafo_personal_care, "Personal Care")
