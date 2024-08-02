import os
import pandas as pd
import  plotly.express as px


lista_arquivo = os.listdir("C:\\Users\\PESSOAL\\Mundo Python\\Aulas de Python\\Hashtag\\Arquivos da aula\\Vendas-20240802T162049Z-001\\Vendas")
tabela_total = pd.DataFrame()
for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(f"C:\\Users\\PESSOAL\\Mundo Python\\Aulas de Python\\Hashtag\\Arquivos da aula\\Vendas-20240802T162049Z-001\\Vendas\\{arquivo}")
        tabela_total = pd.concat([tabela_total, tabela], ignore_index=True)

tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by='Quantidade Vendida', ascending=False)

print(tabela_produtos)
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by='Faturamento', ascending=False)

print(tabela_faturamento)
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']]

print(tabela_lojas)
grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()