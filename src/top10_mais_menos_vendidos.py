import pandas as pd
import matplotlib.pyplot as plt
import os


chunk_size = 100000  
columns_needed = ['order_id', 'product_id', 'product_name', 'department_id']
departments_map = {4: "Produce", 11: "Personal Care"}  
departments_to_process = list(departments_map.keys())


department_sales = {dept: {'top_10': [], 'bottom_10': []} for dept in departments_to_process}


chunks = pd.read_csv('base_de_dados/processed_data_with_department.csv', usecols=columns_needed, chunksize=chunk_size)

for chunk in chunks:
    
    chunk = chunk[chunk['department_id'].isin(departments_to_process)]

    
    for department in departments_to_process:
        department_data = chunk[chunk['department_id'] == department]

        
        product_counts = department_data.groupby(['product_id', 'product_name']).size()

        
        department_sales[department]['top_10'].append(product_counts.nlargest(10))
        department_sales[department]['bottom_10'].append(product_counts.nsmallest(10))

    del chunk  


final_data = []

for department in departments_to_process:
    
    top_10 = pd.concat(department_sales[department]['top_10']).groupby(level=[0, 1]).sum().nlargest(10)
    bottom_10 = pd.concat(department_sales[department]['bottom_10']).groupby(level=[0, 1]).sum().nsmallest(10)

    
    top_10_df = top_10.reset_index().rename(columns={0: "Quantidade Vendida"})
    bottom_10_df = bottom_10.reset_index().rename(columns={0: "Quantidade Vendida"})

    top_10_df["Departamento"] = departments_map[department]
    bottom_10_df["Departamento"] = departments_map[department]

    
    final_data.append(top_10_df)
    final_data.append(bottom_10_df)

    
    plt.figure(figsize=(10, 6))
    plt.bar(top_10_df["product_name"], top_10_df["Quantidade Vendida"])
    plt.title(f'Top 10 Produtos Mais Vendidos - {departments_map[department]}')
    plt.xlabel('Produto')
    plt.ylabel('Quantidade Vendida')
    plt.xticks(rotation=45, ha='right')
    plt.show()

    
    plt.figure(figsize=(10, 6))
    plt.bar(bottom_10_df["product_name"], bottom_10_df["Quantidade Vendida"])
    plt.title(f'Bottom 10 Produtos Menos Vendidos - {departments_map[department]}')
    plt.xlabel('Produto')
    plt.ylabel('Quantidade Vendida')
    plt.xticks(rotation=45, ha='right')
    plt.show()


if not os.path.exists('dados'):
    os.makedirs('dados')


final_df = pd.concat(final_data)
final_df.to_csv('dados/relatorio_vendas_departamentos.csv', index=False)

print("Arquivo 'relatorio_vendas_departamentos.csv' salvo na pasta 'dados' com sucesso!")
