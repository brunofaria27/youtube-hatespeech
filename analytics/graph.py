import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_all = pd.read_csv('processed/andrew_processed_prediction.csv')
df_hate = pd.read_csv('processed/hate_comments.csv')

plt.figure(figsize=(8,6))
df_hate['prediction'].value_counts().plot(kind='bar', color='#fc8d62')
plt.title('Distribuição de Hate Speech por Tipo')
plt.xlabel('Tipo de Hate Speech')
plt.ylabel('Contagem')
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(df_all['likeCount'], df_all['prediction'].apply(lambda x: {'normal': 1, 'offensive': 2, 'hate speech': 3}[x]), alpha=0.5)
plt.title('Relação entre Likes e Tipo de Comentário')
plt.xlabel('Quantidade de Likes')
plt.ylabel('Tipo de Comentário (1: Normal, 2: Ofensivo, 3: Hate Speech)')
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='prediction', y='likeCount', data=df_all, palette="magma", width=0.6, fliersize=4, linewidth=2)
plt.title('Distribution of Like Count by Prediction', fontsize=16, weight='bold', pad=20)
plt.xlabel('Prediction', fontsize=14)
plt.ylabel('Like Count', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
