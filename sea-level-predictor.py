# Importar bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Passo 1: Carregar os dados
df = pd.read_csv('epa-sea-level.csv')

# Passo 2: Criar gráfico de dispersão dos dados
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Dados de Nível do Mar')

# Passo 3: Ajustar uma linha de regressão usando todos os dados (1880-2013)
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Passo 4: Criar array de anos para prever até 2050
years_extended = np.arange(df['Year'].min(), 2051)

# Passo 5: Plotar a primeira linha de regressão (usando todos os dados)
plt.plot(years_extended, intercept + slope*years_extended, 'r', label='Regressão Linear (1880-2050)')

# Passo 6: Ajustar outra linha de regressão usando dados a partir do ano 2000
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

# Passo 7: Plotar a segunda linha de regressão (usando dados de 2000 em diante)
plt.plot(years_extended, intercept_recent + slope_recent*years_extended, 'g', label='Regressão Linear (2000-2050)')

# Passo 8: Adicionar título, rótulos e legenda
plt.title('Predição do Nível do Mar até 2050')
plt.xlabel('Ano')
plt.ylabel('Nível do Mar (em polegadas)')
plt.legend()

# Passo 9: Salvar a figura
plt.savefig('sea_level_predictor.png')

# Exibir o gráfico
plt.show()
