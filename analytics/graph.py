import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração do estilo dos gráficos
sns.set(style="whitegrid")

# Leitura do arquivo CSV
file_path = 'andrew_processed_2_processed.csv'  # Substitua pelo caminho do seu arquivo CSV
df = pd.read_csv(file_path)

# Contagem das previsões
prediction_counts = df['prediction'].value_counts()

# Gráfico de barras
plt.figure(figsize=(12, 6))
sns.barplot(x=prediction_counts.index, y=prediction_counts.values, palette="viridis")
plt.title('Quantidade de Cada Prediction')
plt.xlabel('Prediction')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bar_chart.png')  # Salva o gráfico como uma imagem
plt.show()

# Gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(prediction_counts, labels=prediction_counts.index, autopct='%1.1f%%', colors=sns.color_palette("viridis", len(prediction_counts)))
plt.title('Distribuição de Predictions')
plt.savefig('pie_chart.png')  # Salva o gráfico como uma imagem
plt.show()
