# Importando as bibliotecas necessárias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Função para carregar e processar os dados
def load_and_process_data():
    # Carregar os dados
    df = pd.read_csv('medical_examination.csv')

    # Adicionar coluna 'overweight'
    df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

    # Normalizar os dados de colesterol e pressão arterial
    df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
    df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

    return df

# Função para desenhar gráficos categóricos
def draw_cat_plot():
    df = load_and_process_data()

    # Redefinir o DataFrame para o formato longo
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Agrupar e contar os dados
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Desenhar gráfico categórico
    cat_plot = sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar', data=df_cat)
    fig = cat_plot.fig

    return fig

# Função para desenhar o mapa de calor
def draw_heat_map():
    df = load_and_process_data()

    # Limpar os dados
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calcular a correlação
    corr = df_heat.corr()

    # Gerar a máscara para a parte superior do triângulo
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Configurar a figura
    fig, ax = plt.subplots(figsize=(12, 12))

    # Desenhar o mapa de calor
    sns.heatmap(corr, annot=True, mask=mask, fmt='.1f', cmap='coolwarm', square=True, linewidths=1, ax=ax)

    return fig

# Chamadas para testar as funções
draw_cat_plot()
draw_heat_map()
