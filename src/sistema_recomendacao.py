import tkinter as tk
from tkinter import ttk, messagebox
import pickle
import collections
import difflib
import os


grafo_dir = "grafos_MST_maxima"


departamentos = sorted([f"Departamento {i}" for i in range(1, 22)])
arquivos_departamentos = {f"Departamento {i}": f"grafo_departamento_{i}_MST_maxima.gpickle" for i in range(1, 22)}

G = None
nomes_produtos_grafo = {}


def carregar_grafo():
    global G, nomes_produtos_grafo

    departamento_escolhido = departamento_var.get()
    arquivo_grafo = arquivos_departamentos.get(departamento_escolhido)

    if not arquivo_grafo:
        messagebox.showerror("Erro", "Selecione um departamento válido.")
        return

    caminho_grafo = os.path.join(grafo_dir, arquivo_grafo)

    if not os.path.exists(caminho_grafo):
        messagebox.showerror("Erro", f"Grafo do {departamento_escolhido} não encontrado.")
        return

    try:
        with open(caminho_grafo, "rb") as f:
            G = pickle.load(f)
        
       
        nomes_produtos_grafo = {p.lower().strip(): p for p in G.nodes()}

        messagebox.showinfo("Sucesso", f"Grafo do {departamento_escolhido} carregado com sucesso!")
        print(f"✅ Grafo do {departamento_escolhido} carregado!")
        print(f"📌 Número de nós: {len(G.nodes())}, Arestas: {len(G.edges())}")

    except Exception as e:
        messagebox.showerror("Erro ao carregar grafo", str(e))


def recommend_products(product_list, top_n=5):
    if not G:
        return []

    recommendations = collections.Counter()

    for product in product_list:
        if product in G:
            neighbors = G[product]
            for neighbor, attributes in neighbors.items():
                weight = attributes.get("weight", 1)
                recommendations[neighbor] += weight

    
    return sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:top_n]


def recomendar():
    if G is None:
        messagebox.showwarning("Aviso", "Por favor, carregue um departamento primeiro.")
        return

    produtos_usuario = entry.get().split(",")
    produtos_usuario = [p.strip().lower() for p in produtos_usuario]

    if not produtos_usuario or all(p == "" for p in produtos_usuario):
        messagebox.showwarning("Aviso", "Insira pelo menos um produto válido.")
        return

    produtos_validos = []
    produtos_invalidos = []

    for produto in produtos_usuario:
        if produto in nomes_produtos_grafo:
            produtos_validos.append(nomes_produtos_grafo[produto])
        else:
            produtos_invalidos.append(produto)

    
    if produtos_invalidos:
        sugestoes = {
            invalido: difflib.get_close_matches(invalido, nomes_produtos_grafo.keys(), n=3, cutoff=0.5)
            for invalido in produtos_invalidos
        }
        sugestoes_texto = "\n".join(
            f"{k}: {', '.join(v)}" for k, v in sugestoes.items() if v
        )
        if sugestoes_texto:
            messagebox.showinfo("Sugestões", f"Produtos não encontrados:\n\n{sugestoes_texto}")

    if not produtos_validos:
        resultado_label.config(text="Nenhum produto válido encontrado.")
        return

    
    recomendacoes = recommend_products(produtos_validos, top_n=5)

    if recomendacoes:
        resultado = "\n".join([f"{produto}: {peso}" for produto, peso in recomendacoes])
        resultado_label.config(
            text=f"🎯 Recomendações para {', '.join(produtos_usuario)}:\n{resultado}"
        )
    else:
        resultado_label.config(text="Nenhuma recomendação encontrada.")


root = tk.Tk()
root.title("Sistema de Recomendação de Produtos")
root.geometry("600x450")
root.resizable(False, False)


style = ttk.Style()
style.configure("TButton", font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))
style.configure("TCombobox", font=("Arial", 12))

frame = ttk.Frame(root, padding=20)
frame.pack(expand=True, fill="both")


ttk.Label(frame, text="🔍 Sistema de Recomendação", font=("Helvetica", 18, "bold")).pack(pady=10)


ttk.Label(frame, text="Selecione um Departamento:").pack(anchor="w", pady=5)
departamento_var = tk.StringVar()
departamento_dropdown = ttk.Combobox(frame, textvariable=departamento_var, values=departamentos, state="readonly", width=30)
departamento_dropdown.pack(pady=5)
departamento_dropdown.set("Selecione um Departamento")


carregar_btn = ttk.Button(frame, text="Carregar Departamento", command=carregar_grafo)
carregar_btn.pack(pady=10)


ttk.Label(frame, text="Digite nomes dos produtos (separados por vírgula):").pack(anchor="w", pady=5)
entry = ttk.Entry(frame, width=50)
entry.pack(pady=5)


recomendar_btn = ttk.Button(frame, text="🔎 Recomendar", command=recomendar)
recomendar_btn.pack(pady=10)


resultado_label = ttk.Label(frame, text="", font=("Helvetica", 12), justify="left", wraplength=500)
resultado_label.pack(pady=10)


root.mainloop()
