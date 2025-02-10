import networkx as nx
import pickle
import os
import pandas as pd
import matplotlib.pyplot as plt

# Mapeamento de department_id para nome do departamento
department_names = {
    1: "Frozen", 2: "Other", 3: "Bakery", 4: "Produce", 5: "Alcohol",
    6: "International", 7: "Beverages", 8: "Pets", 9: "Dry Goods Pasta",
    10: "Bulk", 11: "Personal Care", 12: "Meat Seafood", 13: "Pantry",
    14: "Breakfast", 15: "Canned Goods", 16: "Dairy Eggs", 17: "Household",
    18: "Babies", 19: "Snacks", 20: "Deli", 21: "Missing"
}

# Diretório onde os grafos estão salvos
grafo_dir = "."  # Defina o caminho correto se necessário

# Dicionário para armazenar as densidades com nomes dos departamentos
densidades = {}

# Loop para processar os 21 departamentos
for i in range(1, 22):  # Departamentos de 1 a 21
    file_name = f'grafo_departamento_{i}.gpickle'
    file_path = os.path.join(grafo_dir, file_name)

    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            G = pickle.load(f)

        # Calcular a densidade do grafo
        densidade = nx.density(G)
        departamento_nome = department_names.get(i, f"Departamento {i}")  # Usa o nome ou um genérico
        densidades[departamento_nome] = densidade
    else:
        print(f"⚠ Arquivo {file_path} não encontrado!")

# Converter os dados em um DataFrame para exibição em tabela
df_densidade = pd.DataFrame(list(densidades.items()), columns=["Departamento X", "Densidade Y"])
df_densidade = df_densidade.sort_values(by="Densidade Y", ascending=False)

# Exibir a tabela no terminal
print("\nTabela de Densidade dos Grafos:")
print(df_densidade.to_string(index=False))

# Criar a pasta 'dados' se não existir
if not os.path.exists('dados'):
    os.makedirs('dados')

# Caminhos para salvar os arquivos na pasta 'dados'
csv_path = os.path.join('dados', 'densidade_grafos.csv')
png_path = os.path.join('dados', 'densidade_departamentos.png')

# Salvar a tabela em um arquivo CSV
df_densidade.to_csv(csv_path, index=False)
print(f"\nTabela salva como '{csv_path}'.")

# Criar gráfico de barras para visualização da densidade dos departamentos
plt.figure(figsize=(10, 6))
plt.barh(df_densidade["Departamento X"], df_densidade["Densidade Y"], 
         color=['#1f77b4' if d > 0.5 else '#ff7f0e' for d in df_densidade["Densidade Y"]])

plt.xlabel("Densidade Y")
plt.ylabel("Departamento X")
plt.title("Densidade dos Grafos por Departamento")
plt.gca().invert_yaxis()  # Inverter eixo Y para exibir do maior para o menor

# Salvar o gráfico como PNG
plt.savefig(png_path, dpi=300, bbox_inches='tight')

# Exibir o gráfico
plt.show()

print(f"Gráfico salvo como '{png_path}'.")
