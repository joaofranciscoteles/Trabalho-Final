import networkx as nx
import pickle
import os


os.makedirs("grafos_MST_maxima", exist_ok=True)


for i in range(1, 22):  
    file_name = f'grafo_departamento_{i}.gpickle'
    output_file = f'../grafos_MST_maxima/grafo_departamento_{i}_MST_maxima.gpickle'

    if os.path.exists(file_name):
       
        with open(file_name, 'rb') as f:
            G = pickle.load(f)

        
        for u, v, d in G.edges(data=True):
            d['weight'] = -d.get('weight', 1)  

        
        MST_max = nx.minimum_spanning_tree(G, weight='weight')

        
        for u, v, d in MST_max.edges(data=True):
            d['weight'] = -d['weight']  

        
        with open(output_file, 'wb') as f:
            pickle.dump(MST_max, f)

        print(f"✅ MST Máxima do Departamento {i} gerada e salva! ({len(MST_max.nodes())} nós, {len(MST_max.edges())} arestas)")

    else:
        print(f"⚠ Arquivo {file_name} não encontrado!")
