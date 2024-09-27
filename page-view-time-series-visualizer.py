import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Função para carregar e limpar os dados
def load_and_clean_data():
    # Carregar o dataset
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")
    
    # Remover o top 2.5% e bottom 2.5% dos dados
    df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
    
    return df

# Função para plotar o gráfico de linha
def draw_line_plot(df):
    plt.figure(figsize=(15, 6))
    plt.plot(df.index, df['value'], color='r')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.savefig('line_plot.png')
    return plt.gcf()

# Função para plotar o gráfico de caixa por ano e mês
def draw_box_plot(df):
    # Preparação dos dados
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.strftime('%b')
    df_box['month_num'] = df_box.index.month
    df_box = df_box.sort_values('month_num')

    # Criar a figura
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

    # Boxplot por ano
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Boxplot por mês
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Salvar o gráfico
    plt.savefig('box_plot.png')
    return fig

# Função principal para rodar o projeto
def main():
    # Carregar e limpar os dados
    df = load_and_clean_data()

    # Gerar os gráficos
    draw_line_plot(df)
    draw_box_plot(df)

# Rodar o código
if __name__ == "__main__":
    main()
