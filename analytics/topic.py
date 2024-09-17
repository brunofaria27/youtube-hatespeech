import os
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from wordcloud import WordCloud, STOPWORDS
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

nltk.download('stopwords')

# Defina a lista de arquivos
files_all = [
    'processed/andrew_processed_prediction.csv',
    'processed/impaulsive_processed_prediction.csv',
    'processed/lex_processed_prediction.csv'
]

files_hate = [
    'processed/andrew_hate_comments.csv',
    'processed/impaulsive_hate_comments.csv',
    'processed/lex_hate_comments.csv'
]

# Função para exibir os tópicos
def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print(f"Tópico {topic_idx+1}:")
        print(" ".join([feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]]))

for file in files_hate:
    df = pd.read_csv(file)
    df['comment'] = df['comment'].astype(str).fillna('')

    all_comments = df['comment'].tolist()

    # Definindo stopwords personalizadas
    custom_stopwords = set(STOPWORDS).union(set(stopwords.words('english')))
    
    additional_stopwords = {
        'hes', 'seem', 'listen', 'href', 'gonna', 'go', 'yeah', 'get', 'one', 'would', 'could', 'like', 
        'also', 'really', 'even', 'said', 'say', 'just', 'see', 'make', 'want', 'know', 'think', 'going', 
        'said', 'says', 'look', 'good', 'bad', 'dont', 'did', 'cant', 'didnt', 'isnt', 'wasnt', 'hasnt', 
        'wont', 'will', 'should', 'can', 'might', 'should', 'much', 'many', 'people', 'thing', 'things', 
        'way', 'Thank', 'video', 'back', 'eat', 'may', 'Destiny', 'goggin', 'youre', 'love', 'let', 'got', 
        'David goggin', 'Huberman', 'David', 'man', 'goggins', 'need', 'work', 'time', 'life', 'take', 
        'thats', 'year', 'podcast', 'start', 'lot', 'without', 'old', 'put', 'come', 'dude', 'guy', 'take', 
        'little', 'Lets', 'food', 'hard', 'person', 'give', 'something', 'everything', 'arent', 'never', 'bro', 
        'tell', 'high', 'years', 'better', 'system', 'great', 'real', 'live', 'become', 'day', 'trying', 
        'makes', 'doesnt', 'already', 'Theres', 'Ive', 'shes', 'Thanks', 'George', 'Logan', 'Logan Paul', 
        'Paul', 'Mike', 'Mark', 'episode', 'John Cena', 'John', 'Jeffree', 'Lex', 'Andrew', 'Lana', 'Gena', 
        'Jimmy', 'Beast', 'Cena', 'lol', 'yawn', 'guys', 'watch', 'talk', 'tear'
    }
    custom_stopwords = custom_stopwords.union(additional_stopwords)
    custom_stopwords = list(custom_stopwords)

    # Vetorização dos comentários
    vectorizer = CountVectorizer(stop_words=custom_stopwords, min_df=5)
    comments_vectorized = vectorizer.fit_transform(all_comments)

    # Ajustar o modelo LDA
    lda = LatentDirichletAllocation(n_components=5, random_state=42)  # Defina o número de tópicos (n_components)
    lda.fit(comments_vectorized)

    # Exibir os tópicos
    no_top_words = 10
    feature_names = vectorizer.get_feature_names_out()
    print(f"Tópicos para o arquivo {file}:")
    display_topics(lda, feature_names, no_top_words)
    print("\n")
