import networkx as nx
import pickle
import os
import pandas as pd

def exibir_top_10_conexoes(input_file):
    if not input_file.endswith('.gpickle'):
        print("⚠ O arquivo precisa estar no formato .gpickle")
        return

    if not os.path.exists(input_file):
        print(f"⚠ Arquivo {input_file} não encontrado!")
        return

    
    with open(input_file, 'rb') as f:
        G = pickle.load(f)

    if not nx.is_weighted(G):
        print("⚠ O grafo não contém pesos nas arestas!")
        return

    
    top_10_arestas = sorted(G.edges(data=True), key=lambda x: x[2].get('weight', 0), reverse=True)[:10]

    
    if not os.path.exists('dados'):
        os.makedirs('dados')

    
    top_10_df = pd.DataFrame(top_10_arestas, columns=['Produto1', 'Produto2', 'Dados'])
    top_10_df['Peso'] = top_10_df['Dados'].apply(lambda x: x['weight'])

   
    output_file = 'dados/top_10_conexoes.csv'
    top_10_df[['Produto1', 'Produto2', 'Peso']].to_csv(output_file, index=False)

    print(f"🔝 Top 10 Conexões Mais Fortes foram salvas em: {output_file}")


input_file = 'grafos_MST_maxima/grafo_departamento_11_MST_maxima.gpickle'  # Substitua pelo arquivo desejado
exibir_top_10_conexoes(input_file)
