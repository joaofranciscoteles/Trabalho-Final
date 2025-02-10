import os
import pandas as pd
import matplotlib.pyplot as plt


file_path = "base_de_dados/processed_data_with_department.csv"  


vendas_por_departamento = {}


chunk_size = 500000  
print("Processando os dados...")

for chunk in pd.read_csv(file_path, usecols=["department_id"], chunksize=chunk_size):
    
    counts = chunk["department_id"].value_counts().to_dict()

    
    for dep_id, count in counts.items():
        if dep_id in vendas_por_departamento:
            vendas_por_departamento[dep_id] += count
        else:
            vendas_por_departamento[dep_id] = count

print("Processamento concluído!")


df_vendas = pd.DataFrame(list(vendas_por_departamento.items()), columns=["Departamento", "Total de Vendas"])


df_vendas = df_vendas.sort_values(by="Total de Vendas", ascending=False)


print("\nTop 10 Departamentos com Mais Vendas:")
print(df_vendas.head(10).to_string(index=False))


if not os.path.exists('dados'):
    os.makedirs('dados')


csv_path = os.path.join('dados', 'vendas_por_departamento.csv')
png_path = os.path.join('dados', 'vendas_por_departamento.png')


df_vendas.to_csv(csv_path, index=False)
print(f"\nTabela salva como '{csv_path}'.")


plt.figure(figsize=(10, 6))
plt.barh(df_vendas["Departamento"].astype(str), df_vendas["Total de Vendas"], color="skyblue")
plt.xlabel("Total de Vendas")
plt.ylabel("ID do Departamento")
plt.title("Número de Vendas por Departamento")
plt.gca().invert_yaxis()  


plt.savefig(png_path, dpi=300, bbox_inches="tight")
plt.show()

print(f"Gráfico salvo como '{png_path}'.")
