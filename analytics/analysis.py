import json
import time
import pandas as pd
from transformers import pipeline, AutoTokenizer

# Define o pipeline de detecção de discurso de ódio
model_name = "facebook/roberta-hate-speech-dynabench-r4-target"
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline('text-classification', model=model_name, tokenizer=tokenizer)

# Função para classificar um lote de comentários
def classify_comments_batch(comments):
    results = classifier(comments)
    return [result['label'] for result in results]

# Função para processar e salvar resultados em CSV
def process_files(input_files):
    for input_file in input_files:
        print(f"Processing file: {input_file}")
        start_time = time.time()

        with open(input_file, 'r') as file:
            data = json.load(file)

        comments_data = []
        processed_comments = set()  # Para rastrear comentários processados

        for entry in data:
            commentId = entry.get('commentId', '')
            comment = entry.get('comment', '')
            author = entry.get('author', 'Unknown')
            likeCount = entry.get('likeCount', 0)
            isReply = entry.get('isReply', False)
            
            # Converter likeCount para um número
            if isinstance(likeCount, dict):
                likeCount = likeCount.get('$numberLong', 0)
            try:
                likeCount = int(likeCount)
            except ValueError:
                likeCount = 0
            
            # Garantir que o comentário seja único
            if comment not in processed_comments:
                processed_comments.add(comment)
                
                # Classificar comentário individualmente
                classifications = classify_comments_batch([comment])

                # Adicionar resultados a uma lista
                comments_data.append({
                    'file_name': input_file,
                    'commentId': commentId,
                    'comment': comment,
                    'author': author,
                    'likeCount': likeCount,
                    'isReply': isReply,
                    'prediction': classifications[0]
                })

                # Salvar dados em CSV incrementalmente
                df = pd.DataFrame(comments_data)
                csv_file = input_file.replace('.json', '_processed.csv')
                df.to_csv(csv_file, index=False)
                print(f"Processed and saved comment to {csv_file}")

        print(f"File {input_file} processed in {time.time() - start_time:.2f} seconds.")

# Arquivos de entrada a serem processados
input_files = ['andrew_processed_3.json', 'impaulsive_processed_3.json', 'lex_processed_3.json', 'comments_processed_3.json']

# Processar arquivos e salvar resultados
process_files(input_files)
