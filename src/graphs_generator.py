
import pandas as pd
import networkx as nx
import itertools
import pickle  
from collections import defaultdict

file_path = "../base_de_dados/processed_data_with_department.csv"
chunk_size = 500000  

coocorrencias_por_departamento = defaultdict(lambda: defaultdict(int))

for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    
    grouped = chunk.groupby("order_id")[["product_name", "department_id"]].apply(lambda x: x.values.tolist())


    for produtos in grouped:
        produtos_por_departamento = defaultdict(list)

        
        for product_name, department_id in produtos:
            produtos_por_departamento[department_id].append(product_name)

        
        for dep, lista_produtos in produtos_por_departamento.items():
            for prod1, prod2 in itertools.combinations(sorted(lista_produtos), 2):
                coocorrencias_por_departamento[dep][(prod1, prod2)] += 1


grafos = {}

for dep, coocorrencias in coocorrencias_por_departamento.items():
    G = nx.Graph()

    for (prod1, prod2), peso in coocorrencias.items():
        G.add_edge(prod1, prod2, weight=peso)

    grafos[dep] = G

    
    with open(f"grafo_departamento_{dep}.gpickle", "wb") as f:
        pickle.dump(G, f)

    print(f"Grafo do departamento {dep} salvo!")

print("✅ Todos os grafos foram gerados e salvos!")
