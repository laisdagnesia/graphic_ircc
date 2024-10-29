import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

data = pd.read_csv('ircc_bd.csv', sep=',')

filter_rounds = ['French language proficiency (Version 1)', 'French language proficiency (2024-1)', 'French language proficiency (2023-1)']

filtered_base = data[data['Round Type'].isin(filter_rounds)]

data['Round Type'] = data['Round Type'].fillna("Desconhecido").astype(str)

#filtered_base = data[['Round Type', 'Invitations issued', 'Lowest ranked score']]

#gráfico de dispersão usando Plotly
grafico = px.scatter_matrix(filtered_base, dimensions=['Call','Round Type', 'Invitations issued', 'Lowest ranked score'])

grafico.show()

#gráfico de dispersão simples usando Matplotlib
x = filtered_base['Call']
y = filtered_base['Lowest ranked score']
plt.scatter(x, y, color='b')
plt.xlabel('Call')
plt.ylabel('Lowest ranked score')
plt.title('Express Entry French Category')

plt.axhline(y=400, color='red', linestyle= '--', linewidth=2, label= 'Minha pontuação')

plt.grid(True)
plt.show()
