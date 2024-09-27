import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Passo 1: Ler os dados do arquivo
    df = pd.read_csv('epa-sea-level.csv')
    
    # Passo 2: Criar o gráfico de dispersão
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Sea Level Data')

    # Passo 3: Ajustar a primeira linha de regressão (usando todos os dados de 1880 a 2013)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Criar array de anos para prever até 2050
    years_extended = np.arange(df['Year'].min(), 2051)

    # Plotar a primeira linha de regressão
    plt.plot(years_extended, intercept + slope*years_extended, 'r', label='Best Fit Line (1880-2050)')

    # Passo 4: Ajustar a segunda linha de regressão (usando dados a partir de 2000)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Criar array de anos para a segunda regressão de 2000 a 2050
    years_recent = np.arange(2000, 2051)

    # Plotar a segunda linha de regressão
    plt.plot(years_recent, intercept_recent + slope_recent*years_recent, 'g', label='Best Fit Line (2000-2050)')

    # Passo 5: Adicionar título, rótulos e legenda (ajustados para os testes)
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    # Passo 6: Salvar o gráfico e retornar os dados para teste
    plt.savefig('sea_level_plot.png')
    return plt.gca()
