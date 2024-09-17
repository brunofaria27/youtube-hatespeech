import os
import nltk
import pandas as pd
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS
from nltk.corpus import stopwords

nltk.download('stopwords')

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

for file in files_all:
    df = pd.read_csv(file)
    df['comment'] = df['comment'].astype(str).fillna('')

    all_comments = ' '.join(df['comment'].tolist())
    custom_stopwords = set(STOPWORDS).union(set(stopwords.words('english')))

    additional_stopwords = {'hes', 'seem', 'listen', 'href', 'gonna', 'go', 'yeah', 'get',
                            'one', 'would', 'could', 'like', 'also', 'really', 'even', 'said',
                            'say', 'just', 'see', 'make', 'want', 'know', 'think', 'going',
                            'said', 'says', 'look', 'good', 'bad', 'dont', 'did', 'cant', 'didnt',
                            'isnt', 'wasnt', 'hasnt', 'wont', 'will', 'should', 'can', 'might',
                            'should', 'much', 'many', 'people', 'thing', 'things', 'way', 'Thank',
                            'video', 'back', 'eat', 'may', 'Destiny', 'goggin', 'youre', 'love', 'let',
                            'got', 'David goggin', 'Huberman', 'David', 'man', 'goggins', 'need', 'work',
                            'time', 'life', 'take', 'thats', 'year', 'podcast', 'start', 'lot', 'without',
                            'old', 'put', 'come', 'dude', 'guy', 'take', 'little', 'Lets', 'food', 'hard',
                            'person', 'give', 'something', 'everything', 'arent', 'never', 'bro', 'tell',
                            'high', 'years', 'better', 'system', 'great', 'real', 'live', 'become', 'day',
                            'trying', 'makes', 'doesnt', 'already', 'Theres', 'Ive', 'shes', 'Thanks',
                            'George', 'Logan', 'Logan Paul', 'Paul', 'Mike', 'Mark', 'episode', 'John Cena', 'John',
                            'Jeffree', 'Lex', 'Andrew', 'Lana', 'Gena', 'Jimmy', 'Beast', 'Cena', 'lol', 'yawn', 'guys',
                            'watch', 'talk', 'tear'}
    custom_stopwords = custom_stopwords.union(additional_stopwords)

    wordcloud = WordCloud(
        width=1200,
        height=600,
        background_color='white',
        stopwords=custom_stopwords,
        min_word_length=3
    ).generate(all_comments)

    filename = os.path.basename(file)
    file_prefix = filename.split('_')[0]
    output_image_path = f'graphs/word_cloud/wordcloud_{file_prefix}_comments.png'
    # output_image_path = f'graphs/wordcloud_{file_prefix}_comments_hate.png' # Use this one if the list is hate
    wordcloud.to_file(output_image_path)

    print(f"Imagem salva como {output_image_path}")
