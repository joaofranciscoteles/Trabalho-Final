import pandas as pd

prior_file = '../base_de_dados/order_products__prior.csv'
products_file = '../base_de_dados/products.csv'
departments_file = '../base_de_dados/departments.csv'
output_file = '../base_de_dados/processed_data_with_department.csv'

orders = pd.read_csv(prior_file, usecols=['order_id', 'product_id'])
products = pd.read_csv(products_file, usecols=['product_id', 'product_name', 'department_id'])
departments = pd.read_csv(departments_file, usecols=['department_id', 'department'])

merged_data = pd.merge(orders, products, on='product_id', how='left')

merged_data.to_csv(output_file, index=False)

print(f"Dados processados salvos em {output_file}")
