import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

file_path = 'processed/andrew_processed_processed.csv'
df = pd.read_csv(file_path)

prediction_counts = df['prediction'].value_counts()

hate_speech_counts = prediction_counts[prediction_counts < 1000]
non_hate_speech_counts = prediction_counts[prediction_counts >= 1000]

plt.figure(figsize=(12, 6))
sns.boxplot(x='prediction', y='likeCount', data=df, palette="magma")
plt.title('Distribuição das Previsões em Relação ao likeCount')
plt.xlabel('Prediction')
plt.ylabel('likeCount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('boxplot.png')
plt.show()
