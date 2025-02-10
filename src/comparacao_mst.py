import networkx as nx
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path  

estatisticas = []


for i in range(1, 22):  
    original_file = Path(f'grafo_departamento_{i}.gpickle')
    mst_file = Path(f'../grafos_MST_maxima/grafo_departamento_{i}_MST_maxima.gpickle')

    if original_file.exists() and mst_file.exists():  
        with open(original_file, 'rb') as f:
            G_original = pickle.load(f)
        
        with open(mst_file, 'rb') as f:
            G_mst = pickle.load(f)
        
        
        num_nos_original = len(G_original.nodes())
        num_arestas_original = len(G_original.edges())
        pesos_originais = [d.get('weight', 0) for _, _, d in G_original.edges(data=True)]
        peso_medio_original = np.mean(pesos_originais) if pesos_originais else 0

        
        num_nos_mst = len(G_mst.nodes())
        num_arestas_mst = len(G_mst.edges())
        pesos_mst = [d.get('weight', 0) for _, _, d in G_mst.edges(data=True)]
        peso_medio_mst = np.mean(pesos_mst) if pesos_mst else 0

        estatisticas.append([
            i, num_nos_original, num_arestas_original, round(peso_medio_original, 2),
            num_nos_mst, num_arestas_mst, round(peso_medio_mst, 2)
        ])


df_estatisticas = pd.DataFrame(estatisticas, columns=[
    "Departamento", "Nós Originais", "Arestas Originais", "Peso Médio Original",
    "Nós MST Máxima", "Arestas MST Máxima", "Peso Médio MST"
])


print(df_estatisticas.to_string(index=False))


df_estatisticas.to_csv("dados/comparacao_mst.csv", index=False)
print("\n📂 Arquivo 'comparacao_mst.csv' salvo com sucesso!")




plt.figure(figsize=(10, 6))
plt.bar(df_estatisticas["Departamento"], df_estatisticas["Arestas Originais"], color="blue", alpha=0.6, label="Arestas Originais")
plt.bar(df_estatisticas["Departamento"], df_estatisticas["Arestas MST Máxima"], color="red", alpha=0.6, label="Arestas MST Máxima")
plt.xlabel("Departamento")
plt.ylabel("Número de Arestas")
plt.title("Comparação do Número de Arestas Antes e Depois da MST Máxima")
plt.legend()
plt.show()


plt.figure(figsize=(10, 6))
plt.bar(df_estatisticas["Departamento"], df_estatisticas["Peso Médio Original"], color="green", alpha=0.6, label="Peso Médio Original")
plt.bar(df_estatisticas["Departamento"], df_estatisticas["Peso Médio MST"], color="orange", alpha=0.6, label="Peso Médio MST")
plt.xlabel("Departamento")
plt.ylabel("Peso Médio das Arestas")
plt.title("Comparação dos Pesos Médios das Arestas Antes e Depois da MST Máxima")
plt.legend()
plt.show()
