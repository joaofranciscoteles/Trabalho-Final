import os
import pandas as pd


chunk_size = 100000 
columns_needed = ['order_id', 'product_id', 'product_name', 'department_id']
departments_map = {4: "Produce", 11: "Personal Care"}  
departments_to_process = list(departments_map.keys())  

department_sales = {dept: [] for dept in departments_to_process}


if not os.path.exists('dados'):
    os.makedirs('dados')


chunks = pd.read_csv('base_de_dados/processed_data_with_department.csv', usecols=columns_needed, chunksize=chunk_size)

for chunk in chunks:
    
    chunk = chunk[chunk['department_id'].isin(departments_to_process)]

    
    product_counts = chunk.groupby(['department_id', 'product_id', 'product_name']).size().reset_index(name='Quantidade Vendida')

    
    for department in departments_to_process:
        department_sales[department].append(product_counts[product_counts['department_id'] == department])

    del chunk  


for department in departments_to_process:
    
    department_data = pd.concat(department_sales[department])
    
    
    department_data = department_data.groupby(['product_id', 'product_name'])['Quantidade Vendida'].sum().reset_index()

    department_data["Departamento"] = departments_map[department]

    
    filename = os.path.join('dados', f'total_vendas_{departments_map[department].lower().replace(" ", "_")}.csv')
    
    department_data.to_csv(filename, index=False)

    print(f"Arquivo '{filename}' salvo com sucesso!")

print("Processo concluído!")
