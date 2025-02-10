import networkx as nx
import pickle
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import os

top_10_conexoes = [ #Colocar as conexões fortes dos produtos que se deseja visualizar
    ("Lavender Hand Soap", "Lemon Verbena Hand Soap", 450),
    ("Vegan Nutritional Shake Sweet Vanilla Bean", "Vegan Smooth Chocolate Nutritional Shake", 352),
    ("Moroccan Argan Oil + Argan Stem Cell Triple Moisture Conditioner", "Hair Shampoos", 327),
    ("Lemon Verbena Hand Soap", "Clean Day Basil Hand Soap", 245),
    ("Organic Fuel High Protein Chocolate Shake", "Organic Fuel High Protein Vanilla Milk Shake", 190),
    ("Olive Oil & Aloe Vera Hand Soap", "Lavender Hand Soap", 163),
    ("One Plant-Based Chocolate Flavor Nutritional Shake Drink Mix", "All-In-One French Vanilla Nutritional Shake Sachet", 161),
    ("Honeysuckle Hand Soap", "Lavender Hand Soap", 146),
    ("Classic Lavender & Chamomile Liquid Hand Soap", "Crisp Cucumber & Melon Liquid Hand Soap", 136),
    ("Coconut Milk Nourishing Conditioner", "Coconut Milk Nourishing Shampoo", 133),
]


subgraph = nx.Graph()
for produto1, produto2, peso in top_10_conexoes:
    subgraph.add_edge(produto1, produto2, weight=peso)

print(f"Grafo gerado com os 10 produtos mais conectados.")


pos = nx.spring_layout(subgraph, k=0.5, seed=42)


edge_x = []
edge_y = []
edge_weights = []
for edge in subgraph.edges(data=True):
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)
    edge_weights.append(edge[2]['weight'])

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=2, color='#888'),
    hoverinfo='text',
    mode='lines'
)


node_x = []
node_y = []
node_text = []
for node in subgraph.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_text.append(node)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    hoverinfo='text',
    text=node_text,
    textposition="top center",
    marker=dict(
        showscale=True,
        colorscale='YlGnBu',
        reversescale=True,
        color=[],
        size=20,
        colorbar=dict(
            thickness=10,
            title="Node Connections"
        ),
        line_width=2
    )
)


node_adjacencies = []
for node in subgraph.nodes():
    num_neighbors = len(list(subgraph.neighbors(node)))
    node_adjacencies.append(num_neighbors)

node_trace.marker.color = node_adjacencies


fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title=dict(
                    text='<br>Top 10 Conexões Mais Fortes',
                    font=dict(size=16)
                ),
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20, l=5, r=5, t=40),
                annotations=[dict(
                    text="Visualização do grafo com as 10 conexões mais fortes",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002
                )],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
             )
)


fig.write_html("grafo_top_10.html")
print("Gráfico salvo como 'grafo_top_10.html'. Abrindo no navegador...")


os.system("firefox grafo_top_10.html &")


plt.figure(figsize=(8, 8))
nx.draw(subgraph, pos, with_labels=True, node_size=3000, node_color='skyblue', edge_color='gray', font_size=10, font_weight="bold")
plt.title("Top 10 Conexões Mais Fortes (Matplotlib)")
plt.savefig("grafo_top_10.png")
print("Imagem salva como 'grafo_top_10.png'. Abra para visualizar.")
