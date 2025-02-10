import networkx as nx
import pickle
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import os

with open('grafo_departamento_4.gpickle', 'rb') as f:
    G = pickle.load(f)

num_nodes_to_sample = 500  
if len(G.nodes()) > num_nodes_to_sample:
    subgraph = G.subgraph(list(G.nodes())[:num_nodes_to_sample])
    print(f"Grafo grande detectado. Visualizando subgrafo com {num_nodes_to_sample} nós.")
else:
    subgraph = G
    print(f"Grafo pequeno. Visualizando grafo completo com {len(G.nodes())} nós.")


try:
    pos = nx.spring_layout(subgraph, k=0.1, iterations=50) 
    print("Spring layout calculado com sucesso.")
except:
    print("Spring layout demorou muito, usando Kamada-Kawai.")
    pos = nx.kamada_kawai_layout(subgraph)

edge_x = []
edge_y = []
for edge in subgraph.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines'
)

node_x = []
node_y = []
for node in subgraph.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    hoverinfo='text',
    text="",
    textfont=dict(
        family="sans serif",
        size=10
    ),
    marker=dict(
        showscale=True,
        colorscale='YlGnBu',
        reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=10,
            title="Node Connections"
        ),
        line_width=1
    )
)

node_adjacencies = []
node_text = []
for node in subgraph.nodes():
    num_neighbors = len(list(subgraph.neighbors(node)))
    node_adjacencies.append(num_neighbors)
    node_text.append(f'{node}: {num_neighbors} conexões')

node_trace.marker.color = node_adjacencies
node_trace.hovertext = node_text

fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title=dict(
                    text='<br>Visualização de Subgrafo de Coocorrência de Produtos',
                    font=dict(size=16)  
                ),
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20, l=5, r=5, t=40),
                annotations=[dict(
                    text="Visualização do subgrafo (amostragem de 500 nós)",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002
                )],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
             )
)


fig.write_html("grafo.html")
print("Gráfico salvo como 'grafo.html'. Abrindo no navegador...")

os.system("firefox grafo.html &")


if len(G.nodes()) > 5000:
    plt.figure(figsize=(12, 12))
    nx.draw(subgraph, pos, node_size=30, edge_color='#AAAAAA', alpha=0.6)
    plt.title("Visualização Estática (Matplotlib) para Grafos Grandes")
    plt.savefig("grafo.png")
    print("Imagem salva como 'grafo.png'. Abra para visualizar.")
